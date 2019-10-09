# Devoir Cours3 Documents Structurés Siyu WANG
# script pour convertir le ficher csv en xml 
# -*- coding: utf-8 -*-
import csv

def extract_from_file(file_path, sep=';'):
    Identifiant_station = []
    Code_postal = []
    Adresse = []
    Operateurs = []
    Motorisation = []
    Etat_fonctionnel = []
    URL_Operateur = []
    Complement_adresse = []
    Nombre_de_places_reservees = []
    geo_shape = []
    geo_point_2d = []

    with open(file_path) as f_tournage:
        tournage_reader = csv.reader(f_tournage, delimiter=sep)
        for row in tournage_reader:
            Identifiant_station.append(row[0])
            Code_postal.append(row[1])
            Adresse.append(row[2])
            Operateurs.append(row[3])
            Motorisation.append(row[4])
            Etat_fonctionnel.append(row[5])
            URL_Operateur.append(row[6])
            Complement_adresse.append(row[7])
            Nombre_de_places_reservees.append(row[8])
            geo_shape.append(row[9])
            geo_point_2d.append(row[10])

    return Identifiant_station, Code_postal, Adresse, Operateurs, Motorisation, Etat_fonctionnel, URL_Operateur, Complement_adresse, Nombre_de_places_reservees, geo_shape, geo_point_2d 

def write_output_file(Identifiant_station, Code_postal, Adresse, Operateurs, Motorisation, Etat_fonctionnel, URL_Operateur, Complement_adresse, Nombre_de_places_reservees, geo_shape, geo_point_2d, file ):
    with open(file,'w',encoding='utf-8') as xmlfile:
        xmlfile.write("<Station_de_vehicules>\n")
        i = 1
        while (i < len(Identifiant_station)):
            xmlfile.write(f"<ID_station>{Identifiant_station[i]}</ID_station><Code_postal>{Code_postal[i]}</Code_postal><Adresse>{Adresse[i]}</Adresse><Operateurs>{Operateurs[i]}</Operateurs><Motorisation>{Motorisation[i]}</Motorisation><Etat_fonctionnel>{Etat_fonctionnel[i]}</Etat_fonctionnel><URL_Operateur>{URL_Operateur[i]}</URL_Operateur><Complement_adresse>{Complement_adresse[i]}</Complement_adresse><Nombre_de_places_reservees>{Nombre_de_places_reservees[i]}</Nombre_de_places_reservees><geo_shape>{geo_shape[i]}</geo_shape><geo_point_2d>{geo_point_2d[i]}</geo_point_2d>\n")
            i += 1
        xmlfile.write("</Station_de_vehicules>")

Identifiant_station, Code_postal, Adresse, Operateurs, Motorisation, Etat_fonctionnel, URL_Operateur, Complement_adresse, Nombre_de_places_reservees, geo_shape, geo_point_2d  = extract_from_file('./liste-des-stations-de-services-de-vehicules.csv')
print ("output file generated")
write_output_file(Identifiant_station, Code_postal, Adresse, Operateurs, Motorisation, Etat_fonctionnel, URL_Operateur, Complement_adresse, Nombre_de_places_reservees, geo_shape, geo_point_2d , "StationVehicule_output.xml")