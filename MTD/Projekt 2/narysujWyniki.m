function narysujWyniki(Dane,sciezka,sciezka_do_napisu,kosztDrogi)
wspolczynnik = 100;
iteratorKrawedzi = 1;

for i=1:size(Dane.wierzcholki,1)
   if (i == Dane.p_start) || (i == Dane.p_meta)
       plot3(Dane.wierzcholki{i}(1),Dane.wierzcholki{i}(2),Dane.wierzcholki{i}(3),'o','Color','g','MarkerSize',14,'LineWidth',6);
   else
       plot3(Dane.wierzcholki{i}(1),Dane.wierzcholki{i}(2),Dane.wierzcholki{i}(3),'o','Color','b','MarkerSize',10);
   end
   text(Dane.wierzcholki{i}(1),Dane.wierzcholki{i}(2),Dane.wierzcholki{i}(3),"\leftarrow W"+num2str(i),'FontSize',14);
   hold on;
end

for i=1:size(Dane.macierz_sasiedztwa,1)
   for j=1:size(Dane.macierz_sasiedztwa,2)     
       if Dane.macierz_sasiedztwa(i,j) ~= 0
          temp_wektor = [abs(int64((Dane.wierzcholki{i}(1)-Dane.wierzcholki{j}(1))*wspolczynnik)),abs(int64((Dane.wierzcholki{i}(2)-Dane.wierzcholki{j}(2))*wspolczynnik)),abs(int64((Dane.wierzcholki{i}(3)-Dane.wierzcholki{j}(3))*wspolczynnik))];
          liczbaElementow = max(temp_wektor);
          x_lin = linspace(Dane.wierzcholki{i}(1),Dane.wierzcholki{j}(1),liczbaElementow);
          y_lin = linspace(Dane.wierzcholki{i}(2),Dane.wierzcholki{j}(2),liczbaElementow);
          z_lin = linspace(Dane.wierzcholki{i}(3),Dane.wierzcholki{j}(3),liczbaElementow);
          krawedzZnaleziona = false;
          for k=1:size(sciezka,1)
             if sciezka{k}(1) == i && sciezka{k}(2) == j
                 krawedzZnaleziona = true;
             end
          end
          if krawedzZnaleziona == true
            plot3(x_lin,y_lin,z_lin,'Color','r','LineWidth',6)
            text(x_lin(int64(liczbaElementow/2)),y_lin(int64(liczbaElementow/2)),z_lin(int64(liczbaElementow/2)),"\leftarrow K"+num2str(iteratorKrawedzi),'FontSize',12);
            iteratorKrawedzi = iteratorKrawedzi+1;
          else
            plot3(x_lin,y_lin,z_lin,'Color','b','MarkerSize',6);
          end
          hold on;
       end
   end
end

title("Znaleziona trasa drona: " + num2str(sciezka_do_napisu) +" koszt drogi: "+num2str(kosztDrogi),'FontSize',18);
xlabel('X');
ylabel('Y');
zlabel('Z');
hold off;
end

