CREATE TABLE Color (
	Id INT PRIMARY KEY NOT NULL,
	Name VARCHAR(10)
);

CREATE TABLE Texture (
	Id INT PRIMARY KEY NOT NULL,
	Name VARCHAR(10)
);

CREATE TABLE Variant (
	Id INT PRIMARY KEY NOT NULL,
	Name VARCHAR(10)
);

CREATE TABLE Cardboard (
	Id INT PRIMARY KEY NOT NULL,
	Name VARCHAR(20),
	SampleQuantity INT,
	SachelQuantity INT,
	BoxQuantity INT
);

CREATE TABLE Palette (
	Id INT PRIMARY KEY NOT NULL,
	Name VARCHAR(20),
	FlyQuantity INT,
	BoatQuantity INT,
	TruckQuantity INT,
	fk_CardboardId INT,
	FOREIGN KEY (fk_CardboardId) REFERENCES Cardboard(Id)
);

CREATE TABLE Packaging (
	Id INT PRIMARY KEY NOT NULL,
	Name VARCHAR(20),
	Content INT,
	Quantity INT,
	fk_Palette INT,
	FOREIGN KEY (fk_PlaetteId) REFERENCES Palette(Id)
);

CREATE TABLE Country (
	Id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	Name VARCHAR(50),
	fk_PackagingId INT,
	FOREIGN KEY (fk_PackagingId) REFERENCES Packaging(Id)
);


CREATE TABLE Machine (
	Id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	MachineNumber INT,
	Cadence INT,
	Delay INT,
	fk_VariantId INT,
	fk_PackagingId INT,
	FOREIGN KEY (fk_VariantId) REFERENCES Variant(Id),
	FOREIGN KEY (fk_PackagingId) REFERENCES Packaging(Id)
);

CREATE TABLE Candy (
	Id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	Name VARCHAR(10),
	Additives INT,
	Coating INT,
	Aroma INT,
	Gelling INT,
	Sugar INT
);

CREATE TABLE CandyCost (
	Id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	ManufacturePercentage FLOAT,
	ContioningPercentage FLOAT,
	ShippingPercentage FLOAT,
	GeneralPercentage FLOAT,
	SampleCost FLOAT,
	SatchelCost FLOAT,
	BoxCost FLOAT,
	fk_CandyId INT,
	FOREIGN KEY (fk_CandyId) REFERENCES Candy(Id)
);

CREATE TABLE CandyReferences (
	Id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	fk_CandyId INT,
	fk_ColorId INT,
	fk_TextureId INT,
	fk_Variant INT, 
	fk_PackagingId INT,
	FOREIGN KEY (fk_CandyId) REFERENCES Candy(Id),
	FOREIGN KEY (fk_ColorId) REFERENCES Color(Id),
	FOREIGN KEY (fk_TextureId) REFERENCES Texture(Id),
	FOREIGN KEY (fk_VariantId) REFERENCES Variant(Id),
	FOREIGN KEY (fk_PackagingId) REFERENCES Packaging(Id)
);

CREATE TABLE Orders (
	Id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	DateOrder DATE,
	ClientName VARCHAR(50),
	ClientSurname VARCHAR(50),
	Quantity INT,
	TotalCost FLOAT,
	fk_CandyReferencesId INT,
	fk_CountryId INT,
	FOREIGN KEY (fk_CandyReferencesId) REFERENCES CandyReferences(Id),
	FOREIGN KEY (fk_CountryId) REFERENCES Country(Id)
);

CREATE TABLE Stock (
	Id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	Component VARCHAR(10),
	Conditionnement(kg) INT,
	Palette(kg) INT
);
------------Insert COLOR
INSERT INTO Color(Name) VALUES("Red");
INSERT INTO Color(Name) VALUES("Orange");
INSERT INTO Color(Name) VALUES("Yellow");
INSERT INTO Color(Name) VALUES("Green");
INSERT INTO Color(Name) VALUES("Blue");
INSERT INTO Color(Name) VALUES("Purple");
INSERT INTO Color(Name) VALUES("Black");
INSERT INTO Color(Name) VALUES("Brown");


------------Insert  Texture
INSERT INTO Texture(Name) VALUES("Mou");
INSERT INTO Texture(Name) VALUES("Dur");


------------Insert  Variant
INSERT INTO Variant(Name) VALUES("Acide");
INSERT INTO Variant(Name) VALUES("Sucré");
INSERT INTO Variant(Name) VALUES("Gélifié");
INSERT INTO Variant(Name) VALUES("Sucré/gélifié");

------------Insert Candy
INSERT INTO Candy(Name, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Acidofilo", 6, 7, 7, 7, 1);
INSERT INTO Candy(Name, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Bouteille cola", 10, 9, 7, 1, 10);
INSERT INTO Candy(Name, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Brazil pik", 3, 1, 4, 4, 10);
INSERT INTO Candy(Name, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Color Schtroummpf pik", 6, 5, 7, 8, 7);
INSERT INTO Candy(Name, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Langues acides", 4, 10, 9, 7, 2);
INSERT INTO Candy(Name, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("London pik", 9, 7, 1, 2, 8);
INSERT INTO Candy(Name, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Miami pik", 3, 8, 9, 2, 2);
INSERT INTO Candy(Name, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Pasta Basta", 4, 8, 7, 6, 8);
INSERT INTO Candy(Name, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Pasta frutta", 8, 5, 6, 8, 9);
INSERT INTO Candy(Name, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Sour snup", 7, 4, 1, 9, 8);
INSERT INTO Candy(Name, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Dragibus", 5, 8, 6, 9, 7);
INSERT INTO Candy(Name, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Carensac", 2, 9, 4, 9, 2);
INSERT INTO Candy(Name, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Fraizibus", 10, 10, 5, 5, 4);
INSERT INTO Candy(Name, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Grain de millet", 3, 5, 4, 3, 3);
INSERT INTO Candy(Name, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Starmint", 9, 9, 4, 1, 10);
INSERT INTO Candy(Name, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Florent violette", 3, 2, 7, 9, 2);
INSERT INTO Candy(Name, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Kimono", 7, 7, 5, 10, 3);
INSERT INTO Candy(Name, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Pain Zan", 7, 3, 9, 9, 8);
INSERT INTO Candy(Name, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Rotella", 5, 3, 2, 4, 3);
INSERT INTO Candy(Name, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Zanoïd", 10, 7, 7, 6, 4);
INSERT INTO Candy(Name, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Fraise tagada", 1, 3, 7, 2, 8);
INSERT INTO Candy(Name, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Croco", 9, 4, 3, 10, 8);
INSERT INTO Candy(Name, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Chamallows", 4, 9, 1, 2, 10);
INSERT INTO Candy(Name, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Polka", 7, 1, 2, 10, 4);
INSERT INTO Candy(Name, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Banane", 5, 10, 5, 8, 10);
INSERT INTO Candy(Name, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Ourson", 6, 7, 1, 3, 3);
INSERT INTO Candy(Name, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Filament", 2, 3, 3, 9, 6);


-----------Insert CandyCost
INSERT INTO CandyCost(ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, SatchelCost, BoxCost) VALUES("Acidofilo", 0.1, 0.1, 0.11, 0.13, 0.23, 2.31, 3.42 );
INSERT INTO CandyCost(ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, SatchelCost, BoxCost) VALUES("Bouteille cola", 0.15, 0.14, 0.19, 0.1, 0.30, 2.99, 4.43);
INSERT INTO CandyCost(ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, SatchelCost, BoxCost) VALUES("Brazil pik", 0.13, 0.14, 0.15, 0.09, 0.39,  3.94, 5.83);
INSERT INTO CandyCost(ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, SatchelCost, BoxCost) VALUES("Color Schtroummpf pik", 0.09, 0.16, 0.2, 0.09, 0.28, 2.75, 4.07);
INSERT INTO CandyCost(ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, SatchelCost, BoxCost) VALUES("Langues acides", 0.15, 0.08, 0.11, 0.16, 0.38, 3.84, 5.68);
INSERT INTO CandyCost(ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, SatchelCost, BoxCost) VALUES("London pik", 0.16, 0.09, 0.2, 0.13, 0.31, 3.08, 4.56);
INSERT INTO CandyCost(ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, SatchelCost, BoxCost) VALUES("Miami pik", 0.08, 0.08, 0.11, 0.1, 0.29, 2.93, 4.34);
INSERT INTO CandyCost(ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, SatchelCost, BoxCost) VALUES("Pasta Basta", 0.12, 0.19, 0.16, 0.08, 0.21, 2.11, 3.12);
INSERT INTO CandyCost(ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, SatchelCost, BoxCost) VALUES("Pasta frutta", 0.18, 0.13, 0.16, 0.13, 0.24, 2.37, 3.51);
INSERT INTO CandyCost(ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, SatchelCost, BoxCost) VALUES("Sour snup", 0.11, 0.16, 0.17, 0.16, 0.37, 3.66, 5.42);
INSERT INTO CandyCost(ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, SatchelCost, BoxCost) VALUES("Dragibus", 0.2, 0.09, 0.12, 0.15, 0.25, 2.47, 3.66);
INSERT INTO CandyCost(ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, SatchelCost, BoxCost) VALUES("Carensac", 0.16, 0.12, 0.14, 0.18, 0.21, 2.05, 3.03);
INSERT INTO CandyCost(ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, SatchelCost, BoxCost) VALUES("Fraizibus", 0.13, 0.15, 0.14, 0.11, 0.39, 3.92, 5.80);
INSERT INTO CandyCost(ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, SatchelCost, BoxCost) VALUES("Grain de millet", 0.08, 0.15, 0.13, 0.14, 0.22, 2.16, 3.20);
INSERT INTO CandyCost(ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, SatchelCost, BoxCost) VALUES("Starmint", 0.14, 0.09, 0.18, 0.15, 0.25, 2.49, 3.69);
INSERT INTO CandyCost(ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, SatchelCost, BoxCost) VALUES("Florent violette", 0.19, 0.14, 0.2, 0.17, 0.35, 3.47, 5.14);
INSERT INTO CandyCost(ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, SatchelCost, BoxCost) VALUES("Kimono", 0.14, 0.19, 0.12, 0.13, 0.39 ,3.92 ,5.80);
INSERT INTO CandyCost(ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, SatchelCost, BoxCost) VALUES("Pain Zan", 0.12, 0.16, 0.12, 0.14, 0.32, 3.17, 4.69);
INSERT INTO CandyCost(ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, SatchelCost, BoxCost) VALUES("Rotella", 0.11, 0.11, 0.14, 0.19, 0.23, 2.27, 3.36);
INSERT INTO CandyCost(ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, SatchelCost, BoxCost) VALUES("Zanoïd", 0.19, 0.14, 0.08, 0.11, 0.33, 3.25, 4.81);
INSERT INTO CandyCost(ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, SatchelCost, BoxCost) VALUES("Fraise tagada", 0.12, 0.08, 0.12, 0.16, 0.29, 2.9, 4.29);
INSERT INTO CandyCost(ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, SatchelCost, BoxCost) VALUES("Croco", 0.12, 0.2, 0.08, 0.18, 0.24, 2.36, 3.49);
INSERT INTO CandyCost(ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, SatchelCost, BoxCost) VALUES("Chamallows", 0.16, 0.11, 0.13, 0.11, 0.20,  2.04, 3.02);
INSERT INTO CandyCost(ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, SatchelCost, BoxCost) VALUES("Polka", 0.11, 0.15, 0.1, 0.08, 0.38, 3.77, 5.58);
INSERT INTO CandyCost(ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, SatchelCost, BoxCost) VALUES("Banane", 0.09, 0.14, 0.15, 0.14, 0.27, 2.74, 4.06);
INSERT INTO CandyCost(ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, SatchelCost, BoxCost) VALUES("Ourson", 0.15, 0.09, 0.17, 0.2, 0.36, 3.59, 5.31);
INSERT INTO CandyCost(ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, SatchelCost, BoxCost) VALUES("Filament", 0.08, 0.11, 0.11, 0.19, 0.40, 3.99, 5.91);

----------Insert Box
INSERT INTO Box(Name, SampleQuantity, SachelQuantity, BoxQuantity) VALUES ("Box",20, 10, 200);

----------Insert Palette
INSERT INTO Palette(Name, FlyQuantity, BoatQuantity, TruckQuantity, fk_CardboardId) VALUES ("Palette", 20, 30, 40, 1);

----------Insert Packaging
INSERT INTO Packaging(Name, Content, Quantity) VALUES ("Bonbon", 1, 1);
INSERT INTO Packaging(Name, Content, Quantity) VALUES ("Sample", 1, 3);
INSERT INTO Packaging(Name, Content, Quantity) VALUES ("Satchel", 1, 10);
INSERT INTO Packaging(Name, Content, Quantity) VALUES ("Box", 1, 25);
INSERT INTO Packaging(Name, Content, Quantity, fk_Palette) VALUES ("Avion", 0, 1, 1);
INSERT INTO Packaging(Name, Content, Quantity, fk_Palette) VALUES ("Bateau", 0, 1, 1);
INSERT INTO Packaging(Name, Content, Quantity, fk_Palette) VALUES ("Camion", 0, 1, 1);

--------Insert Country
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Allemagne", 7);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Autriche", 7);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Belgique", 7);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Bulgarie", 7);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Chypre", 7);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Croatie", 7);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Danemark", 7);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Espagne", 7);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Estonie", 7);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Finlande", 7);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("France", 7);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Grèce", 7);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Hongrie", 7);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Irelande", 7);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Italie", 7);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Lettonie", 7);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Lituanie", 7);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Luxembourg", 7);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Malte", 7);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Pays-Bas", 7);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Pologne", 7);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Portugal", 7);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("République tchèque", 7);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Roumanie", 7);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Royaume-Uni", 7);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Slovaquie", 7);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Slovénie", 7);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Suède", 7);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("USA", 5);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Canada", 5);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Mexique", 5);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Japon", 6);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Chine", 5);
INSERT INTO Country(Name, fk_PackagingId) VALUES ("Afrique du sud", 6);

-----------Insert 

