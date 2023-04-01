#include <ogx/Plugins/EasyPlugin.h>
#include <ogx/Data/Clouds/CloudHelpers.h>
#include <ogx/Data/Clouds/KNNSearchKernel.h>
#include <random>

using namespace ogx;
using namespace ogx::Data;

struct GetLessCloud : public ogx::Plugin::EasyMethod 
{
	// parameters
	Data::ResourceID m_node_id;
	float points_to_remove_ratio = 0.7;


	// constructor
	GetLessCloud() : EasyMethod(L"Bartlomiej Gus nr albumu 297415", L"Keyboard - Part 1")
	{
	}

	// add input/output parameters
	virtual void DefineParameters(ParameterBank& bank) 
	{
		bank.Add(L"node_id", m_node_id).AsNode();
		bank.Add(L"Points to remove ratio", points_to_remove_ratio).Min(0.0).Max(1.0);
	}

	// return cloud and protect against error with not defined node,element or cloud
	auto get_cloud(ogx::Data::Nodes::ITransTreeNode* node,Context& context)
	{
		if (node == nullptr)
		{
			ReportError(L"INVALID VALUE OF GIVEN NODE!");
		}
		auto element = node->GetElement();
		if (element == nullptr)
		{
			ReportError(L"INVALID VALUE OF ELEMENT!");
		}
		auto cloud = element->GetData<ogx::Data::Clouds::ICloud>();
		if (cloud == nullptr)
		{
			ReportError(L"INVALID VALUE OF CLOUD!");
		}

		return cloud;
	}

	//get cloud with less points
	void get_less_cloud(ogx::Data::Nodes::ITransTreeNode *node,ogx::Data::Clouds::ICloud *cloud, Context& context)
	{
		OGX_LINE.Msg(ogx::Level::Info, L"I am making cloud with less points.");

		Data::Clouds::PointsRange points_range;
		cloud->GetAccess().GetAllPoints(points_range);

		auto state_range = Data::Clouds::RangeState(points_range);
		auto state = state_range.begin();

		std::vector <ogx::Data::Clouds::Point3D> xyz_coordinates;
		std::vector <ogx::Data::Clouds::Color> colors;
		points_range.GetXYZ(xyz_coordinates);
		points_range.GetColors(colors);

		std::vector <ogx::Data::Clouds::Point3D> xyz_coordinates_new_cloud;
		std::vector <ogx::Data::Clouds::Color> colors_new_cloud;

		std::mt19937 mt;
		std::uniform_real_distribution <float> distribution(0.0,1.0);

		for (int i = 0; i < points_range.size(); i++)
		{
			state++;
			auto random_number = distribution(mt);

			if (random_number >= points_to_remove_ratio)
			{
				xyz_coordinates_new_cloud.push_back(xyz_coordinates[i]);
				colors_new_cloud.push_back(colors[i]);
			}	
		}

		auto element_new_cloud = context.Project().ElementCreate<Data::Clouds::ICloud>();

		if (!element_new_cloud)
		{
			ReportError(L"NEW ELEMENT HAS NOT BE CREATED!");
		}

		auto new_cloud = element_new_cloud->GetData<Data::Clouds::ICloud>();

		if (!element_new_cloud)
		{
			ReportError(L"NEW CLOUD HAS NOT BE CREATED!");
		}

		Data::Clouds::PointsRange new_points_range;
		new_cloud->GetAccess().AllocPoints(xyz_coordinates_new_cloud.size(), &new_points_range);

		new_points_range.SetXYZ(xyz_coordinates_new_cloud);
		new_points_range.SetColors(colors_new_cloud);

		auto new_node = node->CreateChild();
		new_node->Rename(L"LessCloud");
		new_node->SetElement(element_new_cloud);

	}

	virtual void Run(Context& context)
	{
		auto node = context.m_project->TransTreeFindNode(m_node_id);
		auto cloud = get_cloud(node,context);

		get_less_cloud(node,cloud,context);

	}
};

OGX_EXPORT_METHOD(GetLessCloud)

struct FindKeyboard : public ogx::Plugin::EasyMethod
{
	// parameters
	Data::ResourceID m_node_id;
	float distance_hausdorf = 0.01;
	int minimum_points_in_group = 100;
	double ratio_of_minimum_black_points_in_group = 0.8;
	double minimum_diagonal = 0.42;
	double maximum_diagonal = 0.48;

	struct hausdorff_struct
	{
		int group; // which group belongs point
		bool was_or_not; // was or not calculted
		ogx::Data::Clouds::Point3D xyz; //xyz of point
		ogx::Data::Clouds::Color color; // color of point
	};

	// constructor
	FindKeyboard() : EasyMethod(L"Bartlomiej Gus nr albumu 297415", L"Keyboard - Part 2")
	{
	}

	// add input/output parameters
	virtual void DefineParameters(ParameterBank& bank)
	{
		bank.Add(L"node_id", m_node_id).AsNode();
		bank.Add(L"Hausdorff distance", distance_hausdorf).Min((float) 0.0001).Max((float)1.0);
		bank.Add(L"Minimum points in the group", minimum_points_in_group).Min(1).Max(500);
		bank.Add(L"Minimum black points in the group", ratio_of_minimum_black_points_in_group).Min(0.0).Max(1.0);
		bank.Add(L"Minimum diagonal", minimum_diagonal).Min(0.0).Max(1.0);
		bank.Add(L"Maximum diagonal", maximum_diagonal).Min(0.0).Max(1.0);
	}

	// return cloud and protect against error with not defined node,element or cloud
	auto get_cloud(Context& context, ogx::Data::Nodes::ITransTreeNode *user_node)
	{
		auto node = user_node;
		if (node == nullptr)
		{
			ReportError(L"INVALID VALUE OF GIVEN NODE!");
		}
		auto element = node->GetElement();
		if (element == nullptr)
		{
			ReportError(L"INVALID VALUE OF ELEMENT!");
		}
		auto cloud = element->GetData<ogx::Data::Clouds::ICloud>();
		if (cloud == nullptr)
		{
			ReportError(L"INVALID VALUE OF CLOUD!");
		}

		return cloud;
	}

	//group points using hausdorf algorithm
	auto hausdorff(ogx::Data::Clouds::ICloud* cloud, Context& context)
	{
		ogx::Data::Clouds::PointsRange range;
		cloud->GetAccess().GetAllPoints(range);
		std::vector<ogx::Data::Clouds::Point3D> coordinates;
		range.GetXYZ(coordinates);

		std::vector <ogx::Data::Clouds::Color> colors;
		range.GetColors(colors);

		std::vector<hausdorff_struct> hausdorff_vector;
		hausdorff_vector.reserve(range.size());

		hausdorff_struct pom;
		pom.group = 0;
		pom.was_or_not = false;

		pom.xyz = coordinates[0];
		pom.color = colors[0];

		for (int i = 0; i < coordinates.size(); i++)
		{
			pom.xyz = coordinates[i];
			pom.color = colors[i];
			hausdorff_vector.push_back(pom);
		}

		int number_group = 0;

		bool did_I_change = false;

		float progress = 0.0;

		OGX_LINE.Msg(ogx::Level::Info, L"I am starting Hausdorff algorithm. It takes about 25 - 30 minutes. Please be patient. ");

		for (int i = 0; i< hausdorff_vector.size(); i++)
		{
			if (hausdorff_vector[i].group == 0)
			{	
				number_group = number_group + 1;

				hausdorff_vector[i].group = number_group;

				while (true)
				{
					for (int j = 0; j < hausdorff_vector.size(); j++)
					{

						if (hausdorff_vector[j].group == number_group && hausdorff_vector[j].was_or_not == false)
						{
							auto tested_point_double_point_3d = hausdorff_vector[j].xyz.cast<double>();

							for (int k = 0; k < hausdorff_vector.size(); k++)
							{
								auto double_point_3d = hausdorff_vector[k].xyz.cast<double>();
								auto distance = ogx::Math::CalcPointToPointDistance3D(tested_point_double_point_3d, double_point_3d);

								if (distance < distance_hausdorf)
								{
									hausdorff_vector[k].group = number_group;
								}
							}

							hausdorff_vector[j].was_or_not = true;
							did_I_change = true;
						}

					}

					if (did_I_change == false)
					{
						break;
					}

					did_I_change = false;
				}

				OGX_LINE.Msg(ogx::Level::Info, L"Which group has been created " + std::to_wstring(number_group));

			}

			progress++;
			if (!context.Feedback().Update(progress / hausdorff_vector.size()))
			{
				ReportError(L"COULD NOT UPDATE PROGRESS BAR");
			}

		}

		return hausdorff_vector;

	}

	//regroup points from group where there are now 0 points after sorting them for example by color
	auto sort_from_one_to_max(std::vector<hausdorff_struct> hausdorff_vector)
	{
		std::vector<int> unit_groups;

		unit_groups.push_back(-1);

		for (int i = 0; i < hausdorff_vector.size(); i++)
		{
			if (hausdorff_vector[i].group != 0 && std::find(unit_groups.begin(), unit_groups.end(), hausdorff_vector[i].group) == unit_groups.end())
			{
				unit_groups.push_back(hausdorff_vector[i].group);
			}
		}

		unit_groups.erase(unit_groups.begin());

		std::sort(unit_groups.begin(), unit_groups.end());

		for (int i = 0; i < unit_groups.size(); i++)
		{
			for (int j = 0; j < hausdorff_vector.size(); j++)
			{
				if (hausdorff_vector[j].group == unit_groups[i])
				{
					hausdorff_vector[j].group = i + 1;
				}
			}
		}

		return hausdorff_vector;
	}

	//set 0 group to points which contains less then parametr *minimum_points_in_group* and then regroup points using function *sort_from_one_to_max*
	auto grouped_hausdorf(std::vector<hausdorff_struct> hausdorff_vector, Context& context, int *max_group)
	{
		OGX_LINE.Msg(ogx::Level::Info, L"I am clearing points.");

		*max_group = 0;

		for (int i = 0; i < hausdorff_vector.size(); i++)
		{
			if (hausdorff_vector[i].group > *max_group)
			{
				*max_group = hausdorff_vector[i].group;
			}
		}

		OGX_LINE.Msg(ogx::Level::Info, L"Count of groups before clearing: " + std::to_wstring(*max_group));

		if (*max_group == 0)
		{
			ReportError(L"THERE IS ONLY ONE GROUP: ZERO!");
		}

		int count_of_group = 0;

		float progress = 0.0;

		for (int i = 1; i <= *max_group; i++)
		{
			for (int j = 0; j < hausdorff_vector.size(); j++)
			{
				if (hausdorff_vector[j].group == i)
				{
					count_of_group = count_of_group + 1;
				}
			}

			if (count_of_group < minimum_points_in_group)
			{
				for (int j = 0; j < hausdorff_vector.size(); j++)
				{
					if (hausdorff_vector[j].group == i)
					{
						hausdorff_vector[j].group = 0;
					}
				}
			}

			count_of_group = 0;

			progress++;
			if (!context.Feedback().Update(progress / *max_group))
			{
				ReportError(L"COULD NOT UPDATE PROGRESS BAR");
			}
		}

		hausdorff_vector = sort_from_one_to_max(hausdorff_vector);

		*max_group = 0;

		for (int i = 0; i < hausdorff_vector.size(); i++)
		{
			if (hausdorff_vector[i].group > *max_group)
			{
				*max_group = hausdorff_vector[i].group;
			}
		}

		OGX_LINE.Msg(ogx::Level::Info, L"Count of groups after clearing: " + std::to_wstring(*max_group));

		return hausdorff_vector;
	}

	//deposit layer after *grouped_hausdorf*
	void color_layer(std::vector<hausdorff_struct> hausdorff_vector, Context& context, ogx::Data::Clouds::ICloud* cloud)
	{
		ogx::Data::Clouds::PointsRange range;
		cloud->GetAccess().GetAllPoints(range);
		const ogx::String layer_name = L"Group";
		auto const layers = cloud->FindLayers(layer_name);

		auto new_layer = layers.empty() ? cloud->CreateLayer(layer_name, 0.0) : layers[0];

		std::vector<StoredReal> pom2;
		pom2.reserve(hausdorff_vector.size());

		for (int i = 0; i < hausdorff_vector.size(); i++)
		{
			pom2.push_back(hausdorff_vector[i].group);
		}

		range.SetLayerVals(pom2, *new_layer);
	}

	//set 0 group to points which doesn't contain more than parameter *ratio_of_minimum_black_points_in_group* black points
	auto sort_due_to_color(std::vector<hausdorff_struct> hausdorff_vector, Context& context, int *max_group, std::vector<hausdorff_struct> *temporary)
	{
		OGX_LINE.Msg(ogx::Level::Info, L"I am sorting due to color.");

		double count_of_points_in_group = 0.0;
		double count_of_points_in_group_black = 0.0;
		float progress = 0.0;

		for (int i = 1; i <= *max_group; i++)
		{
			for (int j = 0; j < hausdorff_vector.size(); j++)
			{
				if (hausdorff_vector[j].group == i)
				{
					float red_color = hausdorff_vector[j].color(0)/255.0;
					float green_color = hausdorff_vector[j].color(1)/255.0;
					float blue_color = hausdorff_vector[j].color(2)/255.0;

					float color_max = std::max(red_color, std::max(green_color, blue_color));
					float color_min = std::min(red_color, std::min(green_color, blue_color));
					float difference = color_max - color_min;

					float hue = -1.0;
					float saturation = -1.0;
					float value = color_max;

					if (difference == 0)
					{
						hue = 0;
					}
					else if (color_max == red_color && green_color >= blue_color)
					{
						hue = 60.0 * ((green_color - blue_color) / difference);
					}
					else if (color_max == red_color && green_color < blue_color)
					{
						hue = 60.0 * ((green_color - blue_color) / difference) + 360.0;
					}
					else if (color_max == green_color)
					{
						hue = 60.0 * ((blue_color - red_color) / difference) + 120.0;
					}
					else if (color_max == green_color)
					{
						hue = 60.0 * ((red_color - green_color) / difference) + 240.0;
					}

					if (color_max == 0.0)
					{
						saturation = 0.0;
					}
					else
					{
						saturation = difference / color_max;
					}

					if (hue < 0.0)
					{
						hue = hue + 360.0;
					}

					if (value >= 0.0 && value <= 0.3)
					{
						count_of_points_in_group_black = count_of_points_in_group_black + 1.0;
					}

					count_of_points_in_group = count_of_points_in_group + 1.0;
				}
			}

			if (count_of_points_in_group_black < ratio_of_minimum_black_points_in_group * count_of_points_in_group)
			{
				for (int j = 0; j < hausdorff_vector.size(); j++)
				{
					if (hausdorff_vector[j].group == i)
					{
						hausdorff_vector[j].group = 0;
					}
					
				}
			}

			count_of_points_in_group = 0.0;
			count_of_points_in_group_black = 0.0;

			progress++;
			if (!context.Feedback().Update(progress / *max_group))
			{
				ReportError(L"COULD NOT UPDATE PROGRESS BAR");
			}
		}

		hausdorff_vector = sort_from_one_to_max(hausdorff_vector);

		*max_group = 0;

		for (int i = 0; i < hausdorff_vector.size(); i++)
		{
			if (hausdorff_vector[i].group > *max_group)
			{
				*max_group = hausdorff_vector[i].group;
			}
		}

		if (*max_group == 0)
		{
			ReportError(L"THERE IS ONLY ONE GROUP: ZERO!");
		}

		OGX_LINE.Msg(ogx::Level::Info, L"Count of groups after sorting by color: " + std::to_wstring(*max_group));

		for (int i = 0; i < hausdorff_vector.size(); i++)
		{
			if (hausdorff_vector[i].group != 0)
			{
				temporary->push_back(hausdorff_vector[i]);
			}
		}

		return hausdorff_vector;
	}

	//deposit layer grouped by color after *sort_due_to_color*
	void color_layer_after_sorted_color(std::vector<hausdorff_struct> hausdorff_vector, Context& context, ogx::Data::Clouds::ICloud* cloud)
	{
		ogx::Data::Clouds::PointsRange range;
		cloud->GetAccess().GetAllPoints(range);
		const ogx::String layer_name = L"Group after sorting color";
		auto const layers = cloud->FindLayers(layer_name);

		auto sorted_color_layer = layers.empty() ? cloud->CreateLayer(layer_name, 1.0) : layers[1];

		std::vector<StoredReal> pom2;
		pom2.reserve(hausdorff_vector.size());

		for (int i = 0; i < hausdorff_vector.size(); i++)
		{
			pom2.push_back(hausdorff_vector[i].group);
		}

		range.SetLayerVals(pom2, *sorted_color_layer);
	}

	//set 0 group to points which digonal is less than *minimum_diagonal* and more than *maximum_diagonal*
	auto sort_due_to_diagonal(std::vector<hausdorff_struct> hausdorff_vector, Context& context, int* max_group, std::vector<hausdorff_struct> temporary)
	{
		OGX_LINE.Msg(ogx::Level::Info, L"I am sorting due to diagonal. It takes about 10-15 minutes. Please be patient.");

		double max_diagonal = 0;

		float progress = 0.0;

		ogx::Math::Point3D temp_1;
		ogx::Math::Point3D temp_2;

		for (int i = 1; i <= *max_group; i++)
		{
			for (int j = 0; j < temporary.size(); j++)
			{
				for (int k = 0; k < temporary.size(); k++)
				{
					if (temporary[j].group == i && temporary[k].group == i)
					{

						auto distance = ogx::Math::CalcPointToPointDistance3D(temporary[j].xyz.cast<double>(), temporary[k].xyz.cast<double>());

						if ((double) distance > max_diagonal)
						{
							max_diagonal = (double) distance;
							temp_1 = temporary[j].xyz.cast<double>();
							temp_2 = temporary[k].xyz.cast<double>();
						}
					}
				}
			}

			if (!(max_diagonal>minimum_diagonal && max_diagonal< maximum_diagonal))
			{
				for (int j = 0; j < temporary.size(); j++)
				{
					if (temporary[j].group == i)
					{
						temporary[j].group = 0;
					}
				}
			}

			max_diagonal = 0;

			progress++;
			if (!context.Feedback().Update(progress / *max_group))
			{
				ReportError(L"COULD NOT UPDATE PROGRESS BAR");
			}
		}

		temporary = sort_from_one_to_max(temporary);

		*max_group = 0;

		for (int i = 0; i < temporary.size(); i++)
		{
			if (temporary[i].group > *max_group)
			{
				*max_group = temporary[i].group;
			}
		}

		if (*max_group == 0)
		{
			ReportError(L"THERE IS ONLY ONE GROUP: ZERO!");
		}

		OGX_LINE.Msg(ogx::Level::Info, L"Count of groups after sorting by color and diagonal: " + std::to_wstring(*max_group));

		for (int i = 0; i < hausdorff_vector.size(); i++)
		{
			hausdorff_vector[i].group = 0;
		}

		progress = 0;

		for (int i = 0; i < temporary.size(); i++)
		{
			for (int j = 0; j < hausdorff_vector.size(); j++)
			{
				if (temporary[i].xyz == hausdorff_vector[j].xyz)
				{
					hausdorff_vector[j].group = temporary[i].group;
				}
			}

			progress++;
			if (!context.Feedback().Update(progress /temporary.size()))
			{
				ReportError(L"COULD NOT UPDATE PROGRESS BAR");
			}
		}

		return hausdorff_vector;

	}

	//deposit layer grouped by color after *sort_due_to_color* *sort_due_to_diagonal*
	void color_layer_after_sorted_color_and_diagonal(std::vector<hausdorff_struct> hausdorff_vector, Context& context, ogx::Data::Clouds::ICloud* cloud)
	{
		ogx::Data::Clouds::PointsRange range;
		cloud->GetAccess().GetAllPoints(range);
		const ogx::String layer_name = L"Group after sorting color and diagonal";
		auto const layers = cloud->FindLayers(layer_name);

		auto sorted_color_and_diagonal_layer = layers.empty() ? cloud->CreateLayer(layer_name, 2.0) : layers[2];

		std::vector<StoredReal> pom2;
		pom2.reserve(hausdorff_vector.size());

		for (int i = 0; i < hausdorff_vector.size(); i++)
		{
			pom2.push_back(hausdorff_vector[i].group);
		}

		range.SetLayerVals(pom2, *sorted_color_and_diagonal_layer);
	}

	virtual void Run(Context& context)
	{
		auto node = context.m_project->TransTreeFindNode(m_node_id);
		auto cloud = get_cloud(context,node);
		auto hausdorf_vector = hausdorff(cloud, context);

		int max_group = 0;
		auto grouped_hausdorff_vector = grouped_hausdorf(hausdorf_vector, context, &max_group);

		color_layer(grouped_hausdorff_vector, context, cloud);

		std::vector<hausdorff_struct> temporary;

		auto sorted_hausdorff_vector_due_to_color = sort_due_to_color(grouped_hausdorff_vector, context, &max_group, &temporary);

		color_layer_after_sorted_color(sorted_hausdorff_vector_due_to_color, context, cloud);

		auto sorted_hausdorff_vector_due_to_color_and_diagonal = sort_due_to_diagonal(sorted_hausdorff_vector_due_to_color, context, &max_group, temporary);

		color_layer_after_sorted_color_and_diagonal(sorted_hausdorff_vector_due_to_color_and_diagonal, context, cloud);

		grouped_hausdorff_vector.clear();
		sorted_hausdorff_vector_due_to_color.clear();
		sorted_hausdorff_vector_due_to_color_and_diagonal.clear();
		temporary.clear();
	}
};

OGX_EXPORT_METHOD(FindKeyboard)
