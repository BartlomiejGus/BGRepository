package projekt;

import com.toedter.calendar.JDateChooser;
import javax.swing.*;
import java.awt.GridBagLayout;
import java.awt.Dimension;
import java.awt.GridBagConstraints;
import java.awt.Image;
import java.awt.Font;
import java.awt.Insets;
import java.awt.Color;
import java.awt.Toolkit;
import java.awt.Component;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import java.io.*;
import java.net.UnknownHostException;
import java.util.*;

class Mapa 
{
    HashMap<Object,Object> map_obiektow;
    HashMap<Object,Object> map_obiektow_po_sortowana;
    
    Mapa()
    {
        map_obiektow = new HashMap();
        map_obiektow_po_sortowana = new HashMap();
    }
    
    public HashMap<Object, Object> sortByValue(HashMap<Object, Object> hm, int po_czym_sortowac, boolean czy_ros_czy_mal)
    {
        List<Map.Entry<Object, Object> > list =
               new LinkedList<Map.Entry<Object, Object> >(hm.entrySet());
 
        Collections.sort(list, new Comparator<Map.Entry<Object, Object> >() {
            public int compare(Map.Entry<Object, Object> o1,
                               Map.Entry<Object, Object> o2)
            {
                ArrayList<String> lista1 = new ArrayList();
                lista1 = (ArrayList<String>)o1.getValue();
                
                ArrayList<String> lista2 = new ArrayList();
                lista2 = (ArrayList<String>)o2.getValue();
                
                int output = 0;
                
                switch (po_czym_sortowac){
                    case 0: // Sortowanie po nazwie Kierunku
                        output = lista1.get(po_czym_sortowac).compareTo(lista2.get(po_czym_sortowac));
                        
                        if(!czy_ros_czy_mal)
                        {
                            output = -output;
                        }
                        break;
                    case 1:// Sortowanie po Odległości
                        int pierwsza_odleglosc = Integer.parseInt(lista1.get(po_czym_sortowac));
                        int druga_odleglosc = Integer.parseInt(lista2.get(po_czym_sortowac));
                        output = pierwsza_odleglosc - druga_odleglosc;
                        
                        if(!czy_ros_czy_mal)
                        {
                            output = -output;
                        }
                        break;
                    case 4:// Sortowanie po Cenie za osobę
                        int pierwsza_cena = Integer.parseInt(lista1.get(po_czym_sortowac));
                        int druga_cena = Integer.parseInt(lista2.get(po_czym_sortowac));
                        output = pierwsza_cena - druga_cena;
                        
                        if(!czy_ros_czy_mal)
                        {
                            output = -output;
                        }
                        break;
                    case 5:// Sortowanie po Ocenie
                        double pierwsza_ocena = Double.parseDouble(lista1.get(po_czym_sortowac));
                        double druga_ocena = Double.parseDouble(lista2.get(po_czym_sortowac));
                        
                        pierwsza_ocena = pierwsza_ocena*10;
                        druga_ocena = druga_ocena*10;
                        
                        int pierwsza_ocena_int = (int) pierwsza_ocena;
                        int druga_ocena_int = (int) druga_ocena;
                        
                        output = pierwsza_ocena_int - druga_ocena_int;
                        
                        if(!czy_ros_czy_mal)
                        {
                            output = -output;
                        }
                        break;
                }
                    
                return output;
            }
        });
         
        HashMap<Object, Object> temp = new LinkedHashMap<Object, Object>();
        for (Map.Entry<Object, Object
                > aa : list) {
            temp.put(aa.getKey(), aa.getValue());
        }
        return temp;
    }
    
    void wyswietlanie_co_jest_w_mapie(HashMap pomocniczna)
    {
        Set<Map.Entry<Object, Object>> entries = pomocniczna.entrySet();
        Iterator<Map.Entry<Object, Object>> moviesIterator = entries.iterator();

        while(moviesIterator.hasNext())
        {
            Map.Entry<Object, Object> entry = moviesIterator.next();
            System.out.println(entry.getKey());
            System.out.println(entry.getValue());  
        }
    }
}

public class Projekt implements ActionListener{

    JFrame frame;
    JPanel lewy;
    JPanel prawy;
    JPanel pomocniczny_z_lewej, pomocniczny_z_prawej;
    JDateChooser kalendarz_od_JDateChooser;
    JDateChooser kalendarz_do_JDateChooser;
    JComboBox dokad_ComboBox;
    JComboBox ile_osob_ComboBox;
    JComboBox po_czym_sortowac_ComboBox;
    JCheckBox dowolna_data_CheckBox;
    JButton szukaj_JButton;
    
    Vector oferty;
    Vector co_jest_w_pliku;
    
    Mapa mapa;
    
    int po_czym_przesortowac;
    
    Dimension d;

    public void actionPerformed(ActionEvent e) {
        Object source = e.getSource();
        
        if(source == szukaj_JButton)
        {
            Date yesterday = new Date();
            Calendar c = Calendar.getInstance(); 
            c.setTime(yesterday); 
            c.add(Calendar.DATE, -1);
            yesterday = c.getTime();
            
            po_czym_przesortowac = 0;
            
            if((kalendarz_od_JDateChooser.getDate().compareTo(yesterday)<0||
                    kalendarz_do_JDateChooser.getDate().compareTo(kalendarz_od_JDateChooser.getDate())<0)&&
                    !dowolna_data_CheckBox.isSelected())
            {

                komunikat_jak_zla_data();
            }
            else
            {
                oferty.removeAll(oferty);
            
                if(po_czym_sortowac_ComboBox.getSelectedItem().equals("Kierunek R"))
                {
                    mapa.map_obiektow_po_sortowana = mapa.sortByValue(mapa.map_obiektow, co_jest_w_pliku.indexOf("Kierunek") - 1,true);
                    po_czym_przesortowac = 0;
                }
                else if(po_czym_sortowac_ComboBox.getSelectedItem().equals("Kierunek M"))
                {
                    mapa.map_obiektow_po_sortowana = mapa.sortByValue(mapa.map_obiektow, co_jest_w_pliku.indexOf("Kierunek") - 1,false);
                    po_czym_przesortowac = 0;
                }
                else if(po_czym_sortowac_ComboBox.getSelectedItem().equals("Odległość R"))
                {
                    mapa.map_obiektow_po_sortowana = mapa.sortByValue(mapa.map_obiektow, co_jest_w_pliku.indexOf("Odległość") - 1,true);
                    po_czym_przesortowac = 1;
                }
                else if(po_czym_sortowac_ComboBox.getSelectedItem().equals("Odległość M"))
                {
                    mapa.map_obiektow_po_sortowana = mapa.sortByValue(mapa.map_obiektow, co_jest_w_pliku.indexOf("Odległość") - 1,false);
                    po_czym_przesortowac = 1;
                }
                else if(po_czym_sortowac_ComboBox.getSelectedItem().equals("Cena za osobę R"))
                {
                    mapa.map_obiektow_po_sortowana = mapa.sortByValue(mapa.map_obiektow, co_jest_w_pliku.indexOf("Cena za osobę") - 1,true);
                    po_czym_przesortowac = 2;
                }
                else if(po_czym_sortowac_ComboBox.getSelectedItem().equals("Cena za osobę M"))
                {
                    mapa.map_obiektow_po_sortowana = mapa.sortByValue(mapa.map_obiektow, co_jest_w_pliku.indexOf("Cena za osobę") - 1,false);
                    po_czym_przesortowac = 2;
                }
                else if(po_czym_sortowac_ComboBox.getSelectedItem().equals("Ocena R"))
                {
                    mapa.map_obiektow_po_sortowana = mapa.sortByValue(mapa.map_obiektow, co_jest_w_pliku.indexOf("Ocena") - 1,true);
                    po_czym_przesortowac = 3;
                }
                else if(po_czym_sortowac_ComboBox.getSelectedItem().equals("Ocena M"))
                {
                    mapa.map_obiektow_po_sortowana = mapa.sortByValue(mapa.map_obiektow, co_jest_w_pliku.indexOf("Ocena") - 1,false);
                    po_czym_przesortowac = 3;
                }
                
                dodawanie_do_ofert();
//                usuwanie_ze_wzgledu_na_Rezerwacje();
                
                if(!dowolna_data_CheckBox.isSelected())
                {
                    usuwanie_ze_wzgledu_na_Date();
                }
                
                usuwanie_ze_wzgledu_na_Kierunek();
                usuwanie_ze_wzgledu_na_Liczbe_osob();

                if(oferty.isEmpty())
                {
                    prawy_gdy_empty_oferty();
                }
                else
                {
                    dodawanie_do_GridBagPrawy(po_czym_przesortowac);
                }
            }
        }
        else if(source == dowolna_data_CheckBox)
        {
            if(dowolna_data_CheckBox.isSelected())
            {
                kalendarz_do_JDateChooser.setEnabled(false);
                kalendarz_od_JDateChooser.setEnabled(false);
            }
            else
            {
                kalendarz_do_JDateChooser.setEnabled(true);
                kalendarz_od_JDateChooser.setEnabled(true);
            }
        }
    }
    
    class Event_Sprawdz_Szczegoly_i_Zarezerwuj implements ActionListener
    {
        ArrayList<String> lista;
        JDialog dialog;
        boolean czy_juz_zarezerwowany;
        String linia;
        
        public Event_Sprawdz_Szczegoly_i_Zarezerwuj(ArrayList<String> pomocniczny)
        {
            this.lista = pomocniczny;
        }
        
        public void actionPerformed (ActionEvent e)
        {
            if(e.getActionCommand().equals("Zarezerwuj"))
            {
                czy_juz_zarezerwowany = false;
                linia = "";
                //otwieranie z pliku i sprawdzenie czy został już zarezerwowany ?
                
                
                try 
                {
                    FileReader fr = new FileReader("Zarezerwuj.txt");
                    BufferedReader bfr = new BufferedReader(fr);

                    while((linia = bfr.readLine()) != null)
                    {
                        if(linia.compareTo(lista.get(co_jest_w_pliku.indexOf("Numer")))==0)
                        {
                            czy_juz_zarezerwowany = true;
                            break;
                        }
                    }

                    fr.close();

                } catch (IOException e1) 
                {   
                    System.out.println("Błąd przy otwieraniu pliku!");

                }

                //Przypadek jak już został zarezerwowany
                if(czy_juz_zarezerwowany == true)
                {
//                    JDialog okno_informacyjne = new JDialog();
//
//                    okno_informacyjne.setTitle("Niestety już zarezerwowana");
//                    okno_informacyjne.setResizable(false);
//                    okno_informacyjne.setModal(true);
//                    okno_informacyjne.setLocationRelativeTo(frame);
//
//                    JPanel panel = new JPanel();
//                    panel.setLayout(new BoxLayout(panel,BoxLayout.Y_AXIS));
//                    panel.add(Box.createRigidArea(new Dimension(0,8)));
//
//                    // I wiersz
//
//                    JLabel dokad = new JLabel ("Niestety ale oferta została już zarezerwowana!");
//                    dokad.setFont(new Font("Serif",Font.TRUETYPE_FONT,17));
//                    panel.add(dokad);
//                    panel.add(Box.createRigidArea(new Dimension(0,8)));
//
//                    // II wiersz
//
//                    JPanel panel_do_zarezerwuj = new JPanel();
//                    panel_do_zarezerwuj.setLayout(new GridBagLayout());
//
//                    JButton zamknij = new JButton("OK");
//
//                    zamknij.addActionListener(new ActionListener()
//                    {
//                        public void actionPerformed(ActionEvent e)
//                        {
//                            okno_informacyjne.dispose();
//                            okno_informacyjne.setVisible(false);
//                        }
//                    });
//
//                    panel_do_zarezerwuj.add(zamknij);
//
//                    panel.add(panel_do_zarezerwuj);
//                    panel.add(Box.createRigidArea(new Dimension(0,8)));
//
//
//                    okno_informacyjne.add(panel);
//
//                    okno_informacyjne.pack();
//                    okno_informacyjne.setVisible(true);
                    
                }
                else
                {
                    try
                    {
                        FileWriter fw = new FileWriter("Zarezerwuj.txt",true);
                        fw.write(lista.get(co_jest_w_pliku.indexOf("Numer"))+"\n");
                        fw.close();
                    }
                    catch(IOException ioe)
                    {
                        System.err.println("Zapis nie powiódł się");
                    }

                    JDialog okno_informacyjne = new JDialog();

                    okno_informacyjne.setTitle("Zarezerwowałeś");
                    okno_informacyjne.setResizable(false);
                    okno_informacyjne.setModal(true);
                    okno_informacyjne.setLocationRelativeTo(frame);

                    JPanel panel = new JPanel();
                    panel.setLayout(new BoxLayout(panel,BoxLayout.Y_AXIS));
                    panel.add(Box.createRigidArea(new Dimension(0,8)));

                    // I wiersz

                    JLabel dokad = new JLabel ("Gratulacje udało Ci się dokonać rezerwacji! Jazda!");
                    dokad.setFont(new Font("Serif",Font.TRUETYPE_FONT,17));
                    panel.add(dokad);
                    panel.add(Box.createRigidArea(new Dimension(0,8)));

                    // II wiersz

                    JPanel panel_do_zarezerwuj = new JPanel();
                    panel_do_zarezerwuj.setLayout(new GridBagLayout());

                    JButton zamknij = new JButton("OK");

                    zamknij.addActionListener(new ActionListener()
                    {
                        public void actionPerformed(ActionEvent e)
                        {
                            okno_informacyjne.dispose();
                            okno_informacyjne.setVisible(false);
                        }
                    });

                    panel_do_zarezerwuj.add(zamknij);

                    panel.add(panel_do_zarezerwuj);
                    panel.add(Box.createRigidArea(new Dimension(0,8)));
                    okno_informacyjne.add(panel);

                    okno_informacyjne.pack();
                    okno_informacyjne.setVisible(true);
                }
                
                dodawanie_do_GridBagPrawy(po_czym_przesortowac);
            }   
            else if(e.getActionCommand().equals("Sprawdź"))
            {
                JDialog okno_informacyjne = new JDialog();
            
                okno_informacyjne.setTitle("Szczegółowe informacje");
                okno_informacyjne.setResizable(false);
                okno_informacyjne.setModal(true);
                okno_informacyjne.setLocationRelativeTo(frame);

                JPanel panel = new JPanel();
                panel.setLayout(new BoxLayout(panel,BoxLayout.Y_AXIS));
                panel.add(Box.createRigidArea(new Dimension(0,8)));

                // I wiersz

                JLabel dokad = new JLabel ("Kierunek podróży: " + lista.get(co_jest_w_pliku.indexOf("Kierunek")));
                dokad.setFont(new Font("Serif",Font.TRUETYPE_FONT,17));
                panel.add(dokad);
                panel.add(Box.createRigidArea(new Dimension(0,8)));

                // II wiersz

                JLabel odleglosc = new JLabel ("Odległość: " + lista.get(co_jest_w_pliku.indexOf("Odległość")));
                odleglosc.setFont(new Font("Serif",Font.TRUETYPE_FONT,17));
                panel.add(odleglosc);
                panel.add(Box.createRigidArea(new Dimension(0,8)));

                //III wiersz

                JLabel rodzaj = new JLabel ("Rodzaj wycieczki: " + lista.get(co_jest_w_pliku.indexOf("Rodzaj")));
                rodzaj.setFont(new Font("Serif",Font.TRUETYPE_FONT,17));
                panel.add(rodzaj);
                panel.add(Box.createRigidArea(new Dimension(0,8)));

                //IV wiersz

                JLabel sezon = new JLabel ("Sezon wyjazdu: " + lista.get(co_jest_w_pliku.indexOf("Sezon")));
                sezon.setFont(new Font("Serif",Font.TRUETYPE_FONT,17));
                panel.add(sezon);
                panel.add(Box.createRigidArea(new Dimension(0,8)));

                //V wiersz

                JLabel cena_za_osobe = new JLabel ("Cena za osobę: " + lista.get(co_jest_w_pliku.indexOf("Cena za osobę")));
                cena_za_osobe.setFont(new Font("Serif",Font.TRUETYPE_FONT,17));
                panel.add(cena_za_osobe);
                panel.add(Box.createRigidArea(new Dimension(0,8)));

                //VI wiersz

                JLabel ocena = new JLabel ("Ocena: " + lista.get(co_jest_w_pliku.indexOf("Ocena")));
                ocena.setFont(new Font("Serif",Font.TRUETYPE_FONT,17));
                panel.add(ocena);
                panel.add(Box.createRigidArea(new Dimension(0,8)));

                //VII wiersz

                JLabel osoby = new JLabel ("Liczba osób: " + lista.get(co_jest_w_pliku.indexOf("LiczbaOsobOd"))+" - "+lista.get(co_jest_w_pliku.indexOf("LiczbaOsobDo")));
                osoby.setFont(new Font("Serif",Font.TRUETYPE_FONT,17));
                panel.add(osoby);
                panel.add(Box.createRigidArea(new Dimension(0,8)));

                JPanel panel_do_zarezerwuj = new JPanel();
                panel_do_zarezerwuj.setLayout(new GridBagLayout());

                JButton zamknij = new JButton("OK");

                zamknij.addActionListener(new ActionListener()
                {
                    public void actionPerformed(ActionEvent e)
                    {
                        okno_informacyjne.dispose();
                        okno_informacyjne.setVisible(false);
                    }
                });

                panel_do_zarezerwuj.add(zamknij);

                panel.add(panel_do_zarezerwuj);
                panel.add(Box.createRigidArea(new Dimension(0,8)));
                okno_informacyjne.add(panel);

                okno_informacyjne.pack();
                okno_informacyjne.setVisible(true);
            }
        }
    }
    
    class Niepoprawne_Rozszerzenie extends Exception
    {

        Niepoprawne_Rozszerzenie() 
        {
            super("Niepoprawne rozszerzenie");
            System.out.println("Niepoprawne rozszerzenie");
        }
        
    }
    
    class Niepoprawna_Nazwa extends Exception
    {

        Niepoprawna_Nazwa() 
        {
            super("Niepoprawna Nazwa");
            System.out.println("Niepoprawna Nazwa");
        }
        
    }
    
    class Niepoprawny_Format extends Exception
    {

        Niepoprawny_Format() 
        {
            super("Niepoprawny Format");
            System.out.println("Niepoprawny Format");
        }
        
    }
    
    void komunikat_jak_zla_data()
    {
        JPanel startowy = new JPanel();
        
        prawy.removeAll();
        prawy.setVisible(true);
        prawy.revalidate();
        prawy.repaint();
       
        //Ustawianie ponowne Layout'u
        prawy.setLayout(new GridBagLayout());

        prawy.setPreferredSize(new Dimension(500,190));
        prawy.setAutoscrolls(false);
        
        String text = new String("<html> Nie poprawnie ustawiona data! <br/> Możliwa przyczyna to: wyszukiwanie w przeszłości <br/> "
                + "albo data odjazdu jest wcześniejsza niż data przyjazdu. <br/> "
                + "Proszę o zmianę wybranych wartości w filtrach."
                + "</html>");
        
        JLabel tak = new JLabel("<html><div style='text-align: center;'>" + text + "</div></html>");

        tak.setFont(new Font("Serif",Font.TRUETYPE_FONT,17));
        
        startowy.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        
        startowy.add(tak);
        
        prawy.add(tak);
        
        kalendarz_od_JDateChooser.setDate(java.util.Calendar.getInstance().getTime());
        
        Date tomorrow = new Date();
        Calendar c = Calendar.getInstance(); 
        c.setTime(tomorrow); 
        c.add(Calendar.DATE, 1);
        tomorrow = c.getTime();
        kalendarz_do_JDateChooser.setDate(tomorrow);
        
        //Wersja z JDialog poniżej
        
//        JDialog okno_informacyjne = new JDialog();
//            
//        okno_informacyjne.setTitle("Warning");
//        okno_informacyjne.setResizable(false);
//        okno_informacyjne.setModal(true);
//        okno_informacyjne.setLocationRelativeTo(frame);
//
//        JPanel panel = new JPanel();
//        panel.setLayout(new BoxLayout(panel,BoxLayout.Y_AXIS));
//        panel.add(Box.createRigidArea(new Dimension(0,8)));
//
//        // I wiersz
//
//        JLabel dokad = new JLabel ("Nie poprawnie ustawiona data!");
//        dokad.setFont(new Font("Serif",Font.TRUETYPE_FONT,16));
//        panel.add(dokad);
//        panel.add(Box.createRigidArea(new Dimension(0,8)));
//
//        // II wiersz
//
//        JLabel odleglosc = new JLabel ("Możliwa przyczyna to: wyszukiwanie w przeszłości albo data odjazdu jest wcześniejsza niż data przyjazdu.");
//        odleglosc.setFont(new Font("Serif",Font.TRUETYPE_FONT,16));
//        panel.add(odleglosc);
//        panel.add(Box.createRigidArea(new Dimension(0,8)));
//
//        kalendarz_od_JDateChooser.setDate(java.util.Calendar.getInstance().getTime());
//        
//        Date tomorrow = new Date();
//        Calendar c = Calendar.getInstance(); 
//        c.setTime(tomorrow); 
//        c.add(Calendar.DATE, 1);
//        tomorrow = c.getTime();
//        kalendarz_do_JDateChooser.setDate(tomorrow);
//
//        okno_informacyjne.add(panel);
//
//        okno_informacyjne.pack();
//        okno_informacyjne.setVisible(true);
    }
    
    void dodawanie_do_ofert()
    {
        Set<Map.Entry<Object, Object>> entries = mapa.map_obiektow_po_sortowana.entrySet();
        Iterator<Map.Entry<Object, Object>> moviesIterator = entries.iterator();

        while(moviesIterator.hasNext())
        {
            Map.Entry<Object, Object> entry = moviesIterator.next();
            ArrayList <String> pomocnicza = new ArrayList((ArrayList<String>)entry.getValue());
            pomocnicza.add(0, entry.getKey().toString());
                    
            oferty.add(pomocnicza);
        }
    }
    
    void usuwanie_ze_wzgledu_na_Rezerwacje()
    {
        String linia = "";
        Vector itemsToRemove = new Vector();
        
        try 
        {
            FileReader fr = new FileReader("Zarezerwuj.txt");
            BufferedReader bfr = new BufferedReader(fr);

            while((linia = bfr.readLine()) != null)
            {
                for(int i = 0; i<oferty.size();i++)
                {
                    ArrayList <String> pomocniczy = (ArrayList <String>) oferty.get(i);
                    
                    if(linia.equals(pomocniczy.get(co_jest_w_pliku.indexOf("Numer"))))
                    {
                        itemsToRemove.add(oferty.get(i));
                    }
                }
               
            }
            
            oferty.removeAll(itemsToRemove);

            fr.close();

        } catch (Exception e1) 
        {
              System.out.println("Błąd przy otwieraniu pliku!");

        }
    }
    
    void usuwanie_ze_wzgledu_na_Date()
    {
        Date od_kiedy = kalendarz_od_JDateChooser.getDate();
        Date do_kiedy = kalendarz_do_JDateChooser.getDate();
        
        Date [] poczatki_por_roku = new Date [4];      
        poczatki_por_roku[0] = new Date(2021 - 1900, 11, 21);  
        poczatki_por_roku[1] = new Date(2022 - 1900, 02, 20);
        poczatki_por_roku[2]= new Date(2022 - 1900, 05, 22);
        poczatki_por_roku[3]= new Date(2022 - 1900, 07, 22);
        
        ArrayList <String> w_jakich_porach_roku_jest_wyjazd = new ArrayList();
        
        szuka:
            for(int i = 0; i<poczatki_por_roku.length; i++)
            {
                if(od_kiedy.compareTo(poczatki_por_roku[i])<1)
                {
                    if(i==0)
                    {
                        w_jakich_porach_roku_jest_wyjazd.add("Jesien");
                    }
                    else if(i==1)
                    {
                        w_jakich_porach_roku_jest_wyjazd.add("Zima");
                    }
                    else if(i==2)
                    {
                        w_jakich_porach_roku_jest_wyjazd.add("Wiosna");
                    }
                    else if(i==3)
                    {
                        w_jakich_porach_roku_jest_wyjazd.add("Lato");
                    }

                    for(int j = i; j<poczatki_por_roku.length;j++)
                    {
                        if(do_kiedy.compareTo(poczatki_por_roku[j])>=0)
                        {
                            if(j==0)
                            {
                                w_jakich_porach_roku_jest_wyjazd.add("Zima");
                            }
                            else if(j==1)
                            {
                                w_jakich_porach_roku_jest_wyjazd.add("Wiosna");
                            }
                            else if(j==2)
                            {
                                w_jakich_porach_roku_jest_wyjazd.add("Lato");
                            }
                            else if(j==3)
                            {
                                w_jakich_porach_roku_jest_wyjazd.add("Jesien");
                            }
                        }
                        else
                        {
                            break szuka; 
                        }
                    }
                }
            }
        
        Vector te_ktorych_nie_ma_por_roku  = new Vector();
        
        te_ktorych_nie_ma_por_roku.add("Wiosna");
        te_ktorych_nie_ma_por_roku.add("Lato");
        te_ktorych_nie_ma_por_roku.add("Jesien");
        te_ktorych_nie_ma_por_roku.add("Zima");
        
        te_ktorych_nie_ma_por_roku.removeAll(w_jakich_porach_roku_jest_wyjazd);
        
        Vector itemsToRemove = new Vector();
        
        for(int i = 0; i<te_ktorych_nie_ma_por_roku.size();i++)
        {
            for(int j = 0; j<oferty.size();j++)
            {
                ArrayList <String> pomocniczy = (ArrayList <String>) oferty.get(j);

                if(pomocniczy.get(co_jest_w_pliku.indexOf("Sezon")).equals(te_ktorych_nie_ma_por_roku.get(i)))
                {
                    itemsToRemove.add(oferty.get(j));
                }
            }
        }
        
        oferty.removeAll(itemsToRemove);
        
    }
    
    void usuwanie_ze_wzgledu_na_Kierunek()
    {
        String s = (String) dokad_ComboBox.getSelectedItem();
        
        Vector itemsToRemove = new Vector();
        
        if(!s.equals("Dowolnie"))
        {
            for(int i = 0; i<oferty.size();i++)
            {
                ArrayList <String> pomocniczy = (ArrayList <String>) oferty.get(i);
                
                if(pomocniczy.get(co_jest_w_pliku.indexOf("Kierunek")).equals(s))
                {
                }
                else
                {
                    itemsToRemove.add(oferty.get(i));
                }
            }
            
            oferty.removeAll(itemsToRemove);
           
        }  
    }
    
    void usuwanie_ze_wzgledu_na_Liczbe_osob()
    {
        String s = (String) ile_osob_ComboBox.getSelectedItem();
        
        Vector itemsToRemove = new Vector();
        
        if(!s.equals("Dow"))
        {
            int pom_z_ComboBox = Integer.parseInt(s);
            for(int i = 0; i<oferty.size();i++)
            {
                ArrayList <String> pomocniczy = (ArrayList <String>) oferty.get(i);
                int pom = Integer.parseInt(pomocniczy.get(co_jest_w_pliku.indexOf("LiczbaOsobDo")));
                
                if(pom<pom_z_ComboBox)
                {
                    itemsToRemove.add(oferty.get(i));
                }
            }
            
            oferty.removeAll(itemsToRemove);
        }  
    }
    
    void createLewyJPanel()
    {
        lewy = new JPanel();
        lewy.setLayout(new BoxLayout(lewy,BoxLayout.Y_AXIS));
        pomocniczny_z_lewej = new JPanel();
    }
    
    void createPrawyJPanel()
    {
        prawy = new JPanel();
        prawy.setLayout(new BoxLayout(prawy, BoxLayout.PAGE_AXIS));
        pomocniczny_z_prawej = new JPanel();
    }
    
    void wczytywanie_z_pliku(String nazwa_pliku) throws Niepoprawne_Rozszerzenie, Niepoprawna_Nazwa, Niepoprawny_Format
    {
        String rozszerzenie = new String();
        
        for(int i = nazwa_pliku.length() - 3; i<nazwa_pliku.length(); i++)
        {
            rozszerzenie = rozszerzenie + nazwa_pliku.charAt(i);
        }
        
        if(!rozszerzenie.equals("txt")) throw new Niepoprawne_Rozszerzenie();
        
        if(!nazwa_pliku.equals("Kierunki_Podrozy.txt")) throw new Niepoprawna_Nazwa();
        
        try
        {
            FileReader io = new FileReader(nazwa_pliku);
            BufferedReader bi = new BufferedReader(io);
            String s = bi.readLine();
            
            String k [] = s.split(" ");

            for(int i = 0;i<k.length;i++)
            {
                if(k[i].equals("CenaZaOsobę"))
                {
                    co_jest_w_pliku.add("Cena za osobę");
                }
                else
                {
                    co_jest_w_pliku.add(k[i]);
                }
            }
            
            mapa = new Mapa();
            
            while((s=bi.readLine())!=null)
            {
                String d [] = s.split(" ");
                
                ArrayList<String> lista = new ArrayList();
                
                Integer nr_ewidencyjny = Integer.parseInt(d[0]);
                
                for(int i = 1; i<d.length; i++)
                {
                    if(i == 1 || i == 3 || i == 4)
                    {
                        for(int j = 0; j<d[i].length();j++)
                        {
                            char kolejny_znak = d[i].charAt(j);
                            int ascii = (int) kolejny_znak;
                            
                            if(!((kolejny_znak>=65&&kolejny_znak<=90)||(kolejny_znak>=97&&kolejny_znak<=122))) throw new Niepoprawny_Format();
                        }
                    }
                    else
                    {
                        for(int j = 0; j<d[i].length();j++)
                        {
                            char kolejny_znak = d[i].charAt(j);
                            int ascii = (int) kolejny_znak;
                            
                            if(!((kolejny_znak>=48&&kolejny_znak<=57)||(kolejny_znak==44||kolejny_znak==46))) throw new Niepoprawny_Format();
                        }
                    }
                    lista.add(d[i]);
                }
                
                mapa.map_obiektow.put(nr_ewidencyjny, lista.clone());
                mapa.map_obiektow_po_sortowana.put(nr_ewidencyjny, lista.clone());
                
                lista.removeAll(lista);
            }
            
            frame = new JFrame("Firma Jazda");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            Toolkit tk = Toolkit.getDefaultToolkit();
            d = tk.getScreenSize();
            int x = (int)d.getWidth();
            int y = (int)d.getHeight();

            frame.setSize(x/2,y/2);
            frame.setResizable(false);

            frame.setLocation(x/4, y/4);
            frame.setVisible(true);

            frame.setLayout(new GridBagLayout());
            
            createLewyJPanel();
            createPrawyJPanel();
            dodawanie_do_GridBag();
            dodawanie_do_GridBagLewy();
            startowy_prawy();

            dodawnie_do_Comboxow();
            
            bi.close();
           
        }
        catch(UnknownHostException e)
        {
            System.out.println(e);
        }
        catch(IOException e)
        {
            System.out.println(e);
            Wczytaj_Z_JChooser();
        }
    }
    
    //nieużywane służy do zmiany wielkości obrazka
    BufferedImage resizeImage(BufferedImage originalImage, int targetWidth, int targetHeight) throws IOException 
    {
        Image resultingImage = originalImage.getScaledInstance(targetWidth, targetHeight, Image.SCALE_DEFAULT);
        BufferedImage outputImage = new BufferedImage(targetWidth, targetHeight, BufferedImage.TYPE_INT_RGB);
        outputImage.getGraphics().drawImage(resultingImage, 0, 0, null);
        return outputImage;
    }
    
    void dodawanie_do_GridBag()
    {
        
        GridBagConstraints bag = new GridBagConstraints();
        
        try
        {
            BufferedImage myPicture = ImageIO.read(new File("/Users/Bartek/Documents/NetBeansProjects/projekt/Media/logo.png"));
            JLabel picLabel = new JLabel(new ImageIcon(myPicture));
            
            bag.fill = GridBagConstraints.HORIZONTAL;
            bag.gridx = 1;
            bag.gridy = 0;
            bag.weightx = 0.5;
            frame.getContentPane().add(picLabel,bag);
        }
        catch(IOException ex)
        {
            System.out.println("Wczytywanie się nie powiodło");
        }
        
        //Tekst zachęcający
        JLabel zachecamy = new JLabel("Z nami zawsze bezpieczne podróże!",JLabel.CENTER);
        zachecamy.setForeground(Color.BLACK);
        zachecamy.setFont(new Font("Serif",Font.PLAIN,30));
        
        bag.fill = GridBagConstraints.HORIZONTAL;
        bag.gridx = 2;
        bag.gridy = 0;
        bag.gridwidth = 2;
        frame.getContentPane().add(zachecamy,bag);
        
        JLabel opcje_wyszukiwania = new JLabel("Opcje wyszukiwania:",JLabel.CENTER);
        opcje_wyszukiwania.setFont(new Font("Serif",Font.TRUETYPE_FONT,20));
        
        bag.fill = GridBagConstraints.HORIZONTAL;
        bag.gridx = 1;
        bag.gridy = 1;
        bag.gridwidth = 2;
        bag.weightx = 0.5;
        frame.getContentPane().add(opcje_wyszukiwania,bag);
        
        JLabel dostepne_oferty = new JLabel("Dostępne oferty:",JLabel.CENTER);
        dostepne_oferty.setFont(new Font("Serif",Font.TRUETYPE_FONT,20));
        
        bag.fill = GridBagConstraints.HORIZONTAL;
        bag.gridx = 3;
        bag.insets = new Insets(0,30,0,0);
        bag.gridy = 1;
        bag.gridwidth = 2;
        bag.weightx = 0.0;
        frame.getContentPane().add(dostepne_oferty,bag);
        
        pomocniczny_z_lewej.setMinimumSize(new Dimension(10,0));
        pomocniczny_z_lewej.setPreferredSize(new Dimension(10,0));
        pomocniczny_z_lewej.setMaximumSize(new Dimension(10,0));
        
        bag.fill = GridBagConstraints.HORIZONTAL;
        bag.gridx = 0;
        bag.insets = new Insets(0,0,0,0);
        bag.gridy = 2;
        bag.gridwidth = 1;
        bag.weightx = 0.0;
        frame.getContentPane().add(pomocniczny_z_lewej,bag);
        
        lewy.setMinimumSize(new Dimension(180,250));
        lewy.setPreferredSize(new Dimension(180,300));
        lewy.setMaximumSize(new Dimension(180,250));
        
        bag.fill = GridBagConstraints.HORIZONTAL;
        bag.gridx = 1;
        bag.insets = new Insets(0,0,0,0);
        bag.gridy = 2;
        bag.gridwidth = 2;
        bag.anchor = GridBagConstraints.PAGE_START;
        bag.weightx = 0.1;
        frame.getContentPane().add(lewy,bag);
        
        JScrollPane scroll = new JScrollPane(prawy);
        prawy.setAutoscrolls(true);
        
        scroll.setMinimumSize(new Dimension(490,250));
        scroll.setPreferredSize(new Dimension(490,510));
        scroll.setMaximumSize(new Dimension(490,510));
        
        bag.fill = GridBagConstraints.HORIZONTAL;
        bag.gridx = 3;
        bag.gridy = 2;
        bag.insets = new Insets(0,20,0,0);
        bag.gridwidth = 2;
        bag.weightx = 0.5;
        frame.getContentPane().add(scroll,bag);
        
        pomocniczny_z_prawej.setMinimumSize(new Dimension(10,0));
        pomocniczny_z_prawej.setPreferredSize(new Dimension(10,0));
        pomocniczny_z_prawej.setMaximumSize(new Dimension(10,0));
        
        bag.fill = GridBagConstraints.HORIZONTAL;
        bag.gridx = 5;
        bag.insets = new Insets(0,0,0,0);
        bag.gridy = 2;
        bag.gridwidth = 1;
        bag.weightx = 0.0;
        frame.getContentPane().add(pomocniczny_z_prawej,bag);
                
    }
    
    void dodawanie_do_GridBagLewy()
    {
        
        lewy.add(Box.createRigidArea(new Dimension(0,8)));
        
        //Stworzenie pomocniczego JPanelu do którego będą dodawane kolejne wiersze opcji wyszukiwania
        
        JPanel pomocniczy = new JPanel();
        pomocniczy.setLayout(new BoxLayout(pomocniczy,BoxLayout.LINE_AXIS));
        
        
        // I wiersz
        
        JLabel od_kiedy = new JLabel ("Od Kiedy ?");
        od_kiedy.setFont(new Font("Serif",Font.TRUETYPE_FONT,16));
        pomocniczy.add(od_kiedy);
        
        pomocniczy.add(Box.createRigidArea(new Dimension(8,0)));
        
        kalendarz_od_JDateChooser = new JDateChooser();
        kalendarz_od_JDateChooser.setDate(java.util.Calendar.getInstance().getTime());
        pomocniczy.add(kalendarz_od_JDateChooser);
        
        lewy.add(pomocniczy);
        
        pomocniczy = new JPanel();
        pomocniczy.setLayout(new BoxLayout(pomocniczy,BoxLayout.LINE_AXIS));
        
        // II wiersz
        
        lewy.add(Box.createRigidArea(new Dimension(0,8)));
        JLabel do_kiedy = new JLabel ("Do Kiedy ?");
        do_kiedy.setFont(new Font("Serif",Font.TRUETYPE_FONT,16));
        pomocniczy.add(do_kiedy);
        
        pomocniczy.add(Box.createRigidArea(new Dimension(8,0)));
        
        kalendarz_do_JDateChooser = new JDateChooser();        
        Date tomorrow = new Date();
        Calendar c = Calendar.getInstance(); 
        c.setTime(tomorrow); 
        c.add(Calendar.DATE, 1);
        tomorrow = c.getTime();
        kalendarz_do_JDateChooser.setDate(tomorrow);
        pomocniczy.add(kalendarz_do_JDateChooser);
        
        lewy.add(pomocniczy);
        
        pomocniczy = new JPanel();
        pomocniczy.setLayout(new BoxLayout(pomocniczy,BoxLayout.LINE_AXIS));
        
        //III wierszv2
        
        lewy.add(Box.createRigidArea(new Dimension(0,8)));
        JLabel dowolna_data = new JLabel ("Dowolna data? ");
        dowolna_data.setFont(new Font("Serif",Font.TRUETYPE_FONT,16));
        pomocniczy.add(dowolna_data);
        
        pomocniczy.add(Box.createRigidArea(new Dimension(20,0)));
        
        dowolna_data_CheckBox= new JCheckBox();
        dowolna_data_CheckBox.addActionListener(this);
        pomocniczy.add(dowolna_data_CheckBox);
        
        lewy.add(pomocniczy);
        
        pomocniczy = new JPanel();
        pomocniczy.setLayout(new BoxLayout(pomocniczy,BoxLayout.LINE_AXIS));
        
        //III wiersz
        
        lewy.add(Box.createRigidArea(new Dimension(0,8)));
        JLabel lokalizacja = new JLabel ("Dokąd ? ");
        lokalizacja.setFont(new Font("Serif",Font.TRUETYPE_FONT,16));
        pomocniczy.add(lokalizacja);
        
        pomocniczy.add(Box.createRigidArea(new Dimension(20,0)));
        
        dokad_ComboBox = new JComboBox();
        pomocniczy.add(dokad_ComboBox);
        
        lewy.add(pomocniczy);
        
        pomocniczy = new JPanel();
        pomocniczy.setLayout(new BoxLayout(pomocniczy,BoxLayout.LINE_AXIS));
        
        //IV wiersz
        
        lewy.add(Box.createRigidArea(new Dimension(0,8)));
        JLabel ile_osob = new JLabel ("Liczba osób: ");
        ile_osob.setFont(new Font("Serif",Font.TRUETYPE_FONT,16));
        pomocniczy.add(ile_osob);
        
        pomocniczy.add(Box.createRigidArea(new Dimension(40,0)));
        
        ile_osob_ComboBox = new JComboBox();
        pomocniczy.add(ile_osob_ComboBox);
        
        lewy.add(pomocniczy);
        
        pomocniczy = new JPanel();
        pomocniczy.setLayout(new BoxLayout(pomocniczy,BoxLayout.LINE_AXIS));
        
        //V wiersz
        
        lewy.add(Box.createRigidArea(new Dimension(0,8)));
        JLabel po_czym_sortowac = new JLabel ("Sortuj po: ");
        po_czym_sortowac.setFont(new Font("Serif",Font.TRUETYPE_FONT,16));
        pomocniczy.add(po_czym_sortowac);
        
        pomocniczy.add(Box.createRigidArea(new Dimension(5,0)));
        
        po_czym_sortowac_ComboBox = new JComboBox();
        pomocniczy.add(po_czym_sortowac_ComboBox);
        
        lewy.add(pomocniczy);
        
        pomocniczy = new JPanel();
        pomocniczy.setLayout(new BoxLayout(pomocniczy,BoxLayout.LINE_AXIS));
        
        //VI wiersz
        
        lewy.add(Box.createRigidArea(new Dimension(0,8)));
        szukaj_JButton = new JButton("Szukaj");
        szukaj_JButton.setAlignmentX(Component.CENTER_ALIGNMENT);
        szukaj_JButton.addActionListener(this);
        lewy.add(szukaj_JButton);
        
        lewy.add(Box.createRigidArea(new Dimension(0,10)));
        
        lewy.setBorder(BorderFactory.createCompoundBorder(
                   BorderFactory.createLineBorder(Color.black),
                   lewy.getBorder()));
        

    }
    
    void startowy_prawy()
    {
        JPanel startowy = new JPanel();
        
        prawy.setLayout(new GridBagLayout());
        
        String text = new String("<html> Miło nam jest Ciebie przywitać w naszej aplikacji. <br/> "
                + "W celu znalezienia oferty dla siebie skorzystaj z filtrów i naciśnij szukaj."
                + "<br/> Jazda! </html>");
        
        JLabel tak = new JLabel("<html><div style='text-align: center;'>" + text + "</div></html>");

        tak.setFont(new Font("Serif",Font.TRUETYPE_FONT,17));
        
        tak.setHorizontalAlignment(SwingConstants.CENTER);
        tak.setVerticalAlignment(SwingConstants.CENTER);
        
        startowy.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        
        startowy.add(tak);
        
        prawy.add(tak);          
    }
    
    void prawy_gdy_empty_oferty()
    {
        JPanel startowy = new JPanel();
        
        prawy.removeAll();
        prawy.setVisible(true);
        prawy.revalidate();
        prawy.repaint();
       
        //Ustawianie ponowne Layout'u
        prawy.setLayout(new GridBagLayout());

        prawy.setPreferredSize(new Dimension(490,190));
        prawy.setAutoscrolls(false);
        
        String text = new String("<html> Przepraszamy, ale nie mamy dostępnych <br/> ofert podróży w wybranych kategoriach. <br/> "
                + "Proszę o zmianę wybranych wartości w filtrach."
                + "<br/> Jazda! </html>");
        
        JLabel tak = new JLabel("<html><div style='text-align: center;'>" + text + "</div></html>");

        tak.setFont(new Font("Serif",Font.TRUETYPE_FONT,17));
        
        startowy.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        
        startowy.add(tak);
        
        prawy.add(tak);
    }
    
    JPanel obsluga_layoutu_JPanel_z_ofertami(ArrayList<String> pomocniczy, int co_sortuje)
    {
        JPanel przykladowy1 = new JPanel();
        
        przykladowy1.setLayout(new BoxLayout(przykladowy1,BoxLayout.X_AXIS));
        przykladowy1.add(Box.createRigidArea(new Dimension(0,100)));
        
        if(pomocniczy.get(3).equals("CityBreak"))
        {
            try
            {
                BufferedImage myPicture = ImageIO.read(new File("/Users/Bartek/Documents/NetBeansProjects/projekt/Media/skyscraper.png"));

                JLabel picLabel = new JLabel(new ImageIcon(myPicture));
                przykladowy1.add(picLabel);
            }
            catch(IOException ex)
            {
                System.out.println("Wczytywanie się nie powiodło");
            }
        }
        else if(pomocniczy.get(3).equals("Wczasy"))
        {
            try
            {
                BufferedImage myPicture = ImageIO.read(new File("/Users/Bartek/Documents/NetBeansProjects/projekt/Media/sunbed.png"));

                JLabel picLabel = new JLabel(new ImageIcon(myPicture));
                przykladowy1.add(picLabel);
            }
            catch(IOException ex)
            {
                System.out.println("Wczytywanie się nie powiodło");
            }
        }
        else if(pomocniczy.get(3).equals("WycieczkaObjazdowa"))
        {
            try
            {
                BufferedImage myPicture = ImageIO.read(new File("/Users/Bartek/Documents/NetBeansProjects/projekt/Media/road-trip.png"));

                JLabel picLabel = new JLabel(new ImageIcon(myPicture));
                przykladowy1.add(picLabel);
            }
            catch(IOException ex)
            {
                System.out.println("Wczytywanie się nie powiodło");
            }
        }
        
        przykladowy1.add(Box.createRigidArea(new Dimension(10,0)));
        
        String miejsce_wyjazdu = pomocniczy.get(co_jest_w_pliku.indexOf("Kierunek"));
        
        String przed_informacja = new String();
        String dodatkowa_informacja = new String();
        
        switch (co_sortuje)
        {
            case 0:
                przed_informacja = "";
                dodatkowa_informacja = "";
                break;
            case 1:
                przed_informacja = "Odległość w km: ";
                dodatkowa_informacja = pomocniczy.get(co_jest_w_pliku.indexOf("Odległość"))+".";
                break;
            case 2:
                przed_informacja = "Cena za osobę w PLN: ";
                dodatkowa_informacja = pomocniczy.get(co_jest_w_pliku.indexOf("Cena za osobę"))+".";
                break;
            case 3:
                przed_informacja = "Ocena: ";
                dodatkowa_informacja = pomocniczy.get(co_jest_w_pliku.indexOf("Ocena"))+".";
                break;
        }
                
        JLabel koszt = new JLabel ("<html> Miejsce wyjazdu: "+ miejsce_wyjazdu+"."+"<br/>"+przed_informacja+dodatkowa_informacja+"</html>");
        
        przykladowy1.add(koszt);
        
        przykladowy1.add(Box.createRigidArea(new Dimension(10,0)));
        JButton sprawdz_szczegoly = new JButton("Sprawdź szczegóły");
        sprawdz_szczegoly.addActionListener(new Event_Sprawdz_Szczegoly_i_Zarezerwuj(pomocniczy));
        sprawdz_szczegoly.setActionCommand("Sprawdź");
        przykladowy1.add(sprawdz_szczegoly);
        
        przykladowy1.add(Box.createRigidArea(new Dimension(10,0)));
        JButton zarezerwuj = new JButton("Zarezerwuj");
        zarezerwuj.addActionListener(new Event_Sprawdz_Szczegoly_i_Zarezerwuj(pomocniczy));
        zarezerwuj.setActionCommand("Zarezerwuj");
        zarezerwuj.setEnabled(!Czy_jest_juz_zarezerwowany(pomocniczy));
        przykladowy1.add(zarezerwuj);
        
        przykladowy1.add(Box.createRigidArea(new Dimension(10,0)));
        
        przykladowy1.setBorder(BorderFactory.createCompoundBorder(
                   BorderFactory.createLineBorder(Color.black),
                   przykladowy1.getBorder()));
        
        przykladowy1.add(Box.createRigidArea(new Dimension(0,100)));
        
        
        return przykladowy1;
    }
    
    boolean Czy_jest_juz_zarezerwowany(ArrayList<String> pomocniczy)
    {
        String linia = "";
        boolean czy_juz_zarezerwowany = false;
        
        try 
        {
            FileReader fr = new FileReader("Zarezerwuj.txt");
            BufferedReader bfr = new BufferedReader(fr);

            while((linia = bfr.readLine()) != null)
            {
                if(linia.compareTo(pomocniczy.get(co_jest_w_pliku.indexOf("Numer")))==0)
                {
                    czy_juz_zarezerwowany = true;
                    break;
                }
            }

            fr.close();

        } catch (IOException e1) 
        {   
            System.out.println("Błąd przy otwieraniu pliku!");

        }
        
        return czy_juz_zarezerwowany;
    }
    
    void dodawanie_do_GridBagPrawy(int co_sortuje)
    {   
        //Ustawianie ponowne Layout'u
        prawy.setLayout(new BoxLayout(prawy, BoxLayout.PAGE_AXIS));
        //odświeżanie panelu
        prawy.removeAll();
        prawy.setVisible(true);
    
        prawy.revalidate();
        prawy.repaint();
        
        for(int i = 0; i<oferty.size();i++)
        {
            JPanel s = obsluga_layoutu_JPanel_z_ofertami((ArrayList<String>) oferty.get(i), co_sortuje);
        
            prawy.add(s);
        }
        
        prawy.setPreferredSize(new Dimension(490,oferty.size()*102));// Ustawienie wielkości JPanel'a w którym są wszystkie aktualne 
        
    }
    
    //Część z ComboBoxami
    
    void dodawnie_do_Comboxow()
    {
        dodawnie_do_dokadComboBox();
        dodawanie_po_czym_sortowac_Combox();
        dodawanie_ile_osoboCombox();
    }
    
    void dodawnie_do_dokadComboBox()
    {
        mapa.map_obiektow_po_sortowana = mapa.sortByValue(mapa.map_obiektow, co_jest_w_pliku.indexOf("Kierunek")-1,true);
        
        Set<Map.Entry<Object, Object>> entries = mapa.map_obiektow_po_sortowana.entrySet();
        Iterator<Map.Entry<Object, Object>> moviesIterator = entries.iterator();
        
        ArrayList <String> pomocniczna = new ArrayList();
        
        boolean czy_juz_byl = false;
        
        dokad_ComboBox.addItem("Dowolnie");
      
        while(moviesIterator.hasNext())
        {
            Map.Entry<Object, Object> entry = moviesIterator.next();
            pomocniczna = (ArrayList<String>)entry.getValue();
            
            for(int i = 0; i<dokad_ComboBox.getItemCount();i++)
            {
                if(dokad_ComboBox.getItemAt(i).equals(pomocniczna.get(co_jest_w_pliku.indexOf("Kierunek")-1)))
                {
                    czy_juz_byl = true;
                }
            }
            
            if(czy_juz_byl == false)
            {
                dokad_ComboBox.addItem(pomocniczna.get(co_jest_w_pliku.indexOf("Kierunek")-1));  
            }
            
            
            czy_juz_byl = false;
        }
        
    }
    
    void dodawanie_po_czym_sortowac_Combox()
    {
        po_czym_sortowac_ComboBox.addItem("Kierunek R");
        po_czym_sortowac_ComboBox.addItem("Kierunek M");
        po_czym_sortowac_ComboBox.addItem("Odległość R");
        po_czym_sortowac_ComboBox.addItem("Odległość M");
        po_czym_sortowac_ComboBox.addItem("Cena za osobę R");
        po_czym_sortowac_ComboBox.addItem("Cena za osobę M");
        po_czym_sortowac_ComboBox.addItem("Ocena R");
        po_czym_sortowac_ComboBox.addItem("Ocena M");
    }
    
    void dodawanie_ile_osoboCombox()
    {
        Set<Map.Entry<Object, Object>> entries = mapa.map_obiektow_po_sortowana.entrySet();
        Iterator<Map.Entry<Object, Object>> moviesIterator = entries.iterator();
        
        ArrayList <String> pomocniczna = new ArrayList();
        
        int max = 1;
      
        while(moviesIterator.hasNext())
        {
            Map.Entry<Object, Object> entry = moviesIterator.next();
            pomocniczna = (ArrayList<String>)entry.getValue();
            
            int obecny = Integer.parseInt(pomocniczna.get(co_jest_w_pliku.indexOf("LiczbaOsobDo")-1));
            
            if(obecny>max)
            {
                max=obecny;
            }
        }
        
        ile_osob_ComboBox.addItem("Dow");
        
        for(int i = 1; i<=max;i++)
        {
            String s = String.valueOf(i);
            ile_osob_ComboBox.addItem(s);
        }
    }
    
    void Wczytaj_Z_JChooser()
    {
        JFileChooser fileChooser = new JFileChooser();
        int result = fileChooser.showOpenDialog(frame);
        if (result == JFileChooser.APPROVE_OPTION) {
            File wybrany_plik = fileChooser.getSelectedFile();
            
            try
            {
                wczytywanie_z_pliku(wybrany_plik.getName());
            }
            catch(Niepoprawne_Rozszerzenie e)
            {
                JOptionPane.showMessageDialog(frame,
                "Niepoprawne rozszerzenie pliku!",
                "Error",
                JOptionPane.ERROR_MESSAGE);
                Wczytaj_Z_JChooser();
            }
            catch(Niepoprawna_Nazwa e2)
            {
                JOptionPane.showMessageDialog(frame,
                "Niepoprawna nazwa pliku!",
                "Error",
                JOptionPane.ERROR_MESSAGE);
                Wczytaj_Z_JChooser();
            }
            catch(Niepoprawny_Format e3)
            {
                JOptionPane.showMessageDialog(frame,
                "Niepoprwane dane w pliku!",
                "Error",
                JOptionPane.ERROR_MESSAGE);
                Wczytaj_Z_JChooser();
            }
            
        }
        else if(result == JFileChooser.CANCEL_OPTION)
        {
            System.exit(0);
        }
    }
    
    public Projekt()
    {   
        try
        {
            oferty = new Vector();
            co_jest_w_pliku = new Vector();
            
            wczytywanie_z_pliku("Kierunki_Podrozy");
         
        }
        catch(Niepoprawne_Rozszerzenie e)
        {
            JOptionPane.showMessageDialog(frame,
            "Niepoprawne rozszerzenie pliku!",
            "Error",
            JOptionPane.ERROR_MESSAGE);
            Wczytaj_Z_JChooser();
        }
        catch(Niepoprawna_Nazwa e2)
        {
            JOptionPane.showMessageDialog(frame,
            "Niepoprawna nazwa pliku!",
            "Error",
            JOptionPane.ERROR_MESSAGE);
            Wczytaj_Z_JChooser();
        }
        catch(Niepoprawny_Format e3)
        {
            JOptionPane.showMessageDialog(frame,
            "Niepoprawane dane w pliku!",
            "Error",
            JOptionPane.ERROR_MESSAGE);
            Wczytaj_Z_JChooser();
        }
    }
    
    public static void main(String[] args) {
        new Projekt();
    }
    
}
