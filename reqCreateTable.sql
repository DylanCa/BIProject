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

CREATE TABLE Packaging (
	Id INT PRIMARY KEY NOT NULL,
	Name VARCHAR(10),
	Content INT,
	Quantity INT,
	FOREIGN KEY (Id) REFERENCES Box(Id)
);

CREATE TABLE Box (
	Id INT PRIMARY KEY NOT NULL,
	Name VARCHAR(3),
	SampleQuantity INT
	SachelQuantity INT,
	BoxQuantity INT
);

CREATE TABLE Country (
	Id INT PRIMARY KEY NOT NULL,
	Name VARCHAR(50),
	FOREIGN KEY (Id) REFERENCES Packaging(Id)
);


CREATE TABLE Machine (
	Id INT PRIMARY KEY NOT NULL,
	MachineNumber INT,
	Cadence INT,
	Delay INT,
	FOREIGN KEY (Id) REFERENCES Variant(Id),
	FOREIGN KEY (Id) REFERENCES Packaging(Id)
);

CREATE TABLE Candy (
	Id INT PRIMARY KEY NOT NULL,
	Name VARCHAR(10),
	Additives INT,
	Coating INT,
	Aroma INT,
	Gelling INT,
	Sugar INT
);

CREATE TABLE CandyCost (
	Id INT PRIMARY KEY NOT NULL,
	ManufacturePercentage FLOAT,
	ContioningPercentage FLOAT,
	ShippingPercentage FLOAT,
	GeneralPercentage FLOAT,
	SampleCost FLOAT,
	SatchelCost FLOAT,
	BoxCost FLOAT,
	FOREIGN KEY (Id) REFERENCES Candy(Id)
);

CREATE TABLE Orders (
	Id INT PRIMARY KEY NOT NULL,
	ClientName VARCHAR(50),
	ClientSurname VARCHAR(50),
	Quantity INT,
	TotalCost FLOAT,
	DateOrder DATE,
	FOREIGN KEY (Id) REFERENCES Candy(Id),
	FOREIGN KEY (Id) REFERENCES Color(Id),
	FOREIGN KEY (Id) REFERENCES Texture(Id),
	FOREIGN KEY (Id) REFERENCES Variant(Id),
	FOREIGN KEY (Id) REFERENCES Packaging(Id),
	FOREIGN KEY (Id) REFERENCES Country(Id)
);

CREATE TABLE CandyReferences (
	Id INT PRIMARY KEY NOT NULL,
	FOREIGN KEY (Id) REFERENCES Candy(Id),
	FOREIGN KEY (Id) REFERENCES Color(Id),
	FOREIGN KEY (Id) REFERENCES Texture(Id),
	FOREIGN KEY (Id) REFERENCES Variant(Id),
	FOREIGN KEY (Id) REFERENCES Packaging(Id)
);

CREATE TABLE Stock (
	Id INT PRIMARY KEY NOT NULL,
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
INSERT INTO Box(Name, SampleQuantity, SachelQuantity, BoxQuantity) VALUES ("Box"
