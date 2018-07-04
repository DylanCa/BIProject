CREATE TABLE Color (
	color_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	colorName VARCHAR(20)
);

CREATE TABLE Texture (
	texture_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	textureName VARCHAR(20)
);

CREATE TABLE Variant (
	variant_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	variantName VARCHAR(20)
);

CREATE TABLE Cardboard (
	cardboard_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	cardboardName VARCHAR(20),	
	SampleQuantity INT,
	BagQuantity INT,
	BoxQuantity INT
);

CREATE TABLE Palette (
	palette_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	paletteName VARCHAR(20),
	FlyQuantity INT,
	BoatQuantity INT,
	TruckQuantity INT,
	fk_cardboard_id INT,
	FOREIGN KEY (fk_cardboard_id) REFERENCES Cardboard(cardboard_id)
);

CREATE TABLE Packaging (
	packaging_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	packagingName VARCHAR(20),
	Content INT,
	Quantity INT,
	fk_palette_id INT,
	FOREIGN KEY (fk_palette_id) REFERENCES Palette(palette_id)
);

CREATE TABLE Country (
	country_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	countryName VARCHAR(50),
	fk_packaging_id INT,
	FOREIGN KEY (fk_packaging_id) REFERENCES Packaging(packaging_id)
);


CREATE TABLE Machine (
	machine_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	machineNumber INT,
	Cadence INT,
	Delay INT,
	fk_variant_id INT,
	fk_packaging_id INT,
	FOREIGN KEY (fk_variant_id) REFERENCES Variant(variant_id),
	FOREIGN KEY (fk_packaging_id) REFERENCES Packaging(packaging_id)
);

CREATE TABLE Candy (
	candy_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	candyName VARCHAR(30),
	Additives INT,
	Coating INT,
	Aroma INT,
	Gelling INT,
	Sugar INT
);

CREATE TABLE CandyCost (
	candyCost_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	ManufacturePercentage FLOAT,
	ContioningPercentage FLOAT,
	ShippingPercentage FLOAT,
	GeneralPercentage FLOAT,
	SampleCost FLOAT,
	BagCost FLOAT,
	BoxCost FLOAT,
	fk_candy_id INT,
	FOREIGN KEY (fk_candy_id) REFERENCES Candy(candy_id)
);

CREATE TABLE CandyReferences (
	candyReferences_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	fk_candy_id INT,
	fk_color_id INT,
	fk_texture_id INT,
	fk_variant_id INT, 
	fk_packaging_id INT,
	FOREIGN KEY (fk_candy_id) REFERENCES Candy(candy_id),
	FOREIGN KEY (fk_color_id) REFERENCES Color(color_id),
	FOREIGN KEY (fk_texture_id) REFERENCES Texture(texture_id),
	FOREIGN KEY (fk_variant_id) REFERENCES Variant(variant_id),
	FOREIGN KEY (fk_packaging_id) REFERENCES Packaging(packaging_id)
);

CREATE TABLE Orders (
	orders_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	DateOrder DATE,
	ClientName VARCHAR(50),
	ClientSurname VARCHAR(50),
	Quantity INT,
	TotalCost FLOAT,
	fk_candyReferences_id INT,
	fk_country_id INT,
	FOREIGN KEY (fk_candyReferences_id) REFERENCES CandyReferences(candyReferences_id),
	FOREIGN KEY (fk_country_id) REFERENCES Country(country_id)
);

CREATE TABLE Stock (
	stock_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	Component VARCHAR(10),
	Conditionnementkg INT,
	Palettekg INT
);
------------Insert COLOR
INSERT INTO Color(colorName) VALUES("Red");
INSERT INTO Color(colorName) VALUES("Orange");
INSERT INTO Color(colorName) VALUES("Yellow");
INSERT INTO Color(colorName) VALUES("Green");
INSERT INTO Color(colorName) VALUES("Blue");
INSERT INTO Color(colorName) VALUES("Purple");
INSERT INTO Color(colorName) VALUES("Black");
INSERT INTO Color(colorName) VALUES("Brown");


------------Insert  Texture
INSERT INTO Texture(textureName) VALUES("Mou");
INSERT INTO Texture(textureName) VALUES("Dur");


------------Insert  Variant
INSERT INTO Variant(variantName) VALUES("Acide");
INSERT INTO Variant(variantName) VALUES("Sucré");
INSERT INTO Variant(variantName) VALUES("Gélifié");
INSERT INTO Variant(variantName) VALUES("Sucré/gélifié");

------------Insert Candy
INSERT INTO Candy(candyName, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Acidofilo", 6, 7, 7, 7, 1);
INSERT INTO Candy(candyName, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Bouteille cola", 10, 9, 7, 1, 10);
INSERT INTO Candy(candyName, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Brazil pik", 3, 1, 4, 4, 10);
INSERT INTO Candy(candyName, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Color Schtroummpf pik", 6, 5, 7, 8, 7);
INSERT INTO Candy(candyName, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Langues acides", 4, 10, 9, 7, 2);
INSERT INTO Candy(candyName, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("London pik", 9, 7, 1, 2, 8);
INSERT INTO Candy(candyName, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Miami pik", 3, 8, 9, 2, 2);
INSERT INTO Candy(candyName, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Pasta Basta", 4, 8, 7, 6, 8);
INSERT INTO Candy(candyName, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Pasta frutta", 8, 5, 6, 8, 9);
INSERT INTO Candy(candyName, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Sour snup", 7, 4, 1, 9, 8);
INSERT INTO Candy(candyName, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Dragibus", 5, 8, 6, 9, 7);
INSERT INTO Candy(candyName, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Carensac", 2, 9, 4, 9, 2);
INSERT INTO Candy(candyName, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Fraizibus", 10, 10, 5, 5, 4);
INSERT INTO Candy(candyName, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Grain de millet", 3, 5, 4, 3, 3);
INSERT INTO Candy(candyName, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Starmint", 9, 9, 4, 1, 10);
INSERT INTO Candy(candyName, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Florent violette", 3, 2, 7, 9, 2);
INSERT INTO Candy(candyName, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Kimono", 7, 7, 5, 10, 3);
INSERT INTO Candy(candyName, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Pain Zan", 7, 3, 9, 9, 8);
INSERT INTO Candy(candyName, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Rotella", 5, 3, 2, 4, 3);
INSERT INTO Candy(candyName, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Zanoïd", 10, 7, 7, 6, 4);
INSERT INTO Candy(candyName, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Fraise tagada", 1, 3, 7, 2, 8);
INSERT INTO Candy(candyName, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Croco", 9, 4, 3, 10, 8);
INSERT INTO Candy(candyName, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Chamallows", 4, 9, 1, 2, 10);
INSERT INTO Candy(candyName, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Polka", 7, 1, 2, 10, 4);
INSERT INTO Candy(candyName, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Banane", 5, 10, 5, 8, 10);
INSERT INTO Candy(candyName, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Ourson", 6, 7, 1, 3, 3);
INSERT INTO Candy(candyName, Additives, Coating,	Aroma, Gelling,	Sugar) VALUES("Filament", 2, 3, 3, 9, 6);


-----------Insert CandyCost
INSERT INTO CandyCost(fk_candy_id, ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, BagCost, BoxCost) VALUES(1, 0.1, 0.1, 0.11, 0.13, 0.23, 2.31, 3.42 );
INSERT INTO CandyCost(fk_candy_id, ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, BagCost, BoxCost) VALUES(2, 0.15, 0.14, 0.19, 0.1, 0.30, 2.99, 4.43);
INSERT INTO CandyCost(fk_candy_id, ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, BagCost, BoxCost) VALUES(3,0.13, 0.14, 0.15, 0.09, 0.39,  3.94, 5.83);
INSERT INTO CandyCost(fk_candy_id, ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, BagCost, BoxCost) VALUES(4, 0.09, 0.16, 0.2, 0.09, 0.28, 2.75, 4.07);
INSERT INTO CandyCost(fk_candy_id, ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, BagCost, BoxCost) VALUES(5, 0.15, 0.08, 0.11, 0.16, 0.38, 3.84, 5.68);
INSERT INTO CandyCost(fk_candy_id, ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, BagCost, BoxCost) VALUES(6, 0.16, 0.09, 0.2, 0.13, 0.31, 3.08, 4.56);
INSERT INTO CandyCost(fk_candy_id, ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, BagCost, BoxCost) VALUES(7, 0.08, 0.08, 0.11, 0.1, 0.29, 2.93, 4.34);
INSERT INTO CandyCost(fk_candy_id, ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, BagCost, BoxCost) VALUES(8, 0.12, 0.19, 0.16, 0.08, 0.21, 2.11, 3.12);
INSERT INTO CandyCost(fk_candy_id, ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, BagCost, BoxCost) VALUES(9, 0.18, 0.13, 0.16, 0.13, 0.24, 2.37, 3.51);
INSERT INTO CandyCost(fk_candy_id, ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, BagCost, BoxCost) VALUES(10, 0.11, 0.16, 0.17, 0.16, 0.37, 3.66, 5.42);
INSERT INTO CandyCost(fk_candy_id, ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, BagCost, BoxCost) VALUES(11, 0.2, 0.09, 0.12, 0.15, 0.25, 2.47, 3.66);
INSERT INTO CandyCost(fk_candy_id, ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, BagCost, BoxCost) VALUES(12, 0.16, 0.12, 0.14, 0.18, 0.21, 2.05, 3.03);
INSERT INTO CandyCost(fk_candy_id, ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, BagCost, BoxCost) VALUES(13, 0.13, 0.15, 0.14, 0.11, 0.39, 3.92, 5.80);
INSERT INTO CandyCost(fk_candy_id, ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, BagCost, BoxCost) VALUES(14, 0.08, 0.15, 0.13, 0.14, 0.22, 2.16, 3.20);
INSERT INTO CandyCost(fk_candy_id, ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, BagCost, BoxCost) VALUES(15, 0.14, 0.09, 0.18, 0.15, 0.25, 2.49, 3.69);
INSERT INTO CandyCost(fk_candy_id, ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, BagCost, BoxCost) VALUES(16, 0.19, 0.14, 0.2, 0.17, 0.35, 3.47, 5.14);
INSERT INTO CandyCost(fk_candy_id, ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, BagCost, BoxCost) VALUES(17, 0.14, 0.19, 0.12, 0.13, 0.39 ,3.92 ,5.80);
INSERT INTO CandyCost(fk_candy_id, ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, BagCost, BoxCost) VALUES(18, 0.12, 0.16, 0.12, 0.14, 0.32, 3.17, 4.69);
INSERT INTO CandyCost(fk_candy_id, ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, BagCost, BoxCost) VALUES(19, 0.11, 0.11, 0.14, 0.19, 0.23, 2.27, 3.36);
INSERT INTO CandyCost(fk_candy_id, ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, BagCost, BoxCost) VALUES(20, 0.19, 0.14, 0.08, 0.11, 0.33, 3.25, 4.81);
INSERT INTO CandyCost(fk_candy_id, ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, BagCost, BoxCost) VALUES(21, 0.12, 0.08, 0.12, 0.16, 0.29, 2.9, 4.29);
INSERT INTO CandyCost(fk_candy_id, ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, BagCost, BoxCost) VALUES(22, 0.12, 0.2, 0.08, 0.18, 0.24, 2.36, 3.49);
INSERT INTO CandyCost(fk_candy_id, ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, BagCost, BoxCost) VALUES(23, 0.16, 0.11, 0.13, 0.11, 0.20,  2.04, 3.02);
INSERT INTO CandyCost(fk_candy_id, ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, BagCost, BoxCost) VALUES(24, 0.11, 0.15, 0.1, 0.08, 0.38, 3.77, 5.58);
INSERT INTO CandyCost(fk_candy_id, ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, BagCost, BoxCost) VALUES(25, 0.09, 0.14, 0.15, 0.14, 0.27, 2.74, 4.06);
INSERT INTO CandyCost(fk_candy_id, ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, BagCost, BoxCost) VALUES(26, 0.15, 0.09, 0.17, 0.2, 0.36, 3.59, 5.31);
INSERT INTO CandyCost(fk_candy_id, ManufacturePercentage, ContioningPercentage, ShippingPercentage, GeneralPercentage, SampleCost, BagCost, BoxCost) VALUES(27, 0.08, 0.11, 0.11, 0.19, 0.40, 3.99, 5.91);

----------Insert Cardboard
INSERT INTO Cardboard(cardboardName, SampleQuantity, BagQuantity, BoxQuantity) VALUES ("Box",20, 10, 200);

----------Insert Palette
INSERT INTO Palette(paletteName, FlyQuantity, BoatQuantity, TruckQuantity, fk_cardboard_id) VALUES ("Palette", 20, 30, 40, 1);

----------Insert Packaging
INSERT INTO Packaging(packagingName, Content, Quantity) VALUES ("Bonbon", 1, 1);
INSERT INTO Packaging(packagingName, Content, Quantity) VALUES ("Sample", 1, 3);
INSERT INTO Packaging(packagingName, Content, Quantity) VALUES ("Bag", 1, 10);
INSERT INTO Packaging(packagingName, Content, Quantity) VALUES ("Box", 1, 25);
INSERT INTO Packaging(packagingName, Content, Quantity, fk_palette_id) VALUES ("Avion", 0, 1, 1);
INSERT INTO Packaging(packagingName, Content, Quantity, fk_palette_id) VALUES ("Bateau", 0, 1, 1);
INSERT INTO Packaging(packagingName, Content, Quantity, fk_palette_id) VALUES ("Camion", 0, 1, 1);

--------Insert Country
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Allemagne", 7);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Autriche", 7);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Belgique", 7);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Bulgarie", 7);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Chypre", 7);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Croatie", 7);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Danemark", 7);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Espagne", 7);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Estonie", 7);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Finlande", 7);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("France", 7);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Grèce", 7);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Hongrie", 7);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Irelande", 7);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Italie", 7);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Lettonie", 7);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Lituanie", 7);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Luxembourg", 7);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Malte", 7);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Pays-Bas", 7);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Pologne", 7);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Portugal", 7);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("République tchèque", 7);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Roumanie", 7);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Royaume-Uni", 7);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Slovaquie", 7);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Slovénie", 7);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Suède", 7);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("USA", 5);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Canada", 5);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Mexique", 5);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Japon", 6);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Chine", 5);
INSERT INTO Country(country_name, fk_packaging_id) VALUES ("Afrique du sud", 6);

-----------Insert Machine
INSERT INTO Machine(MachineNumber, Cadence, Delay, fk_variant_id, fk_packaging_id) VALUES (1, 750, 25, 1, ); 
INSERT INTO Machine(MachineNumber, Cadence, Delay, fk_variant_id, fk_packaging_id) VALUES (2, 1230, 45, 2, ); 
INSERT INTO Machine(MachineNumber, Cadence, Delay, fk_variant_id, fk_packaging_id) VALUES (3, 625, 25, 3, ); 
INSERT INTO Machine(MachineNumber, Cadence, Delay, fk_variant_id, fk_packaging_id) VALUES (4, 1230, 45, 4, ); 
INSERT INTO Machine(MachineNumber, Cadence, Delay, fk_variant_id, fk_packaging_id) VALUES (4, 625, 25, 4, ); 
INSERT INTO Machine(MachineNumber, Cadence, Delay, fk_variant_id, fk_packaging_id) VALUES (1, 500, 15, , 3); 
INSERT INTO Machine(MachineNumber, Cadence, Delay, fk_variant_id, fk_packaging_id) VALUES (2, 500, 15, , 3); 
INSERT INTO Machine(MachineNumber, Cadence, Delay, fk_variant_id, fk_packaging_id) VALUES (3, 750, 25, , 3); 
INSERT INTO Machine(MachineNumber, Cadence, Delay, fk_variant_id, fk_packaging_id) VALUES (4, 200, 10, , 4); 
INSERT INTO Machine(MachineNumber, Cadence, Delay, fk_variant_id, fk_packaging_id) VALUES (5, 200, 10, , 4); 
INSERT INTO Machine(MachineNumber, Cadence, Delay, fk_variant_id, fk_packaging_id) VALUES (6, 150, 15, , 2); 

----------Insert Matière premiere
INSERT INTO Stock ( Component, Conditionnementkg, Palettekg	) VALUES ("Additives", 5, 1200);
INSERT INTO Stock ( Component, Conditionnementkg, Palettekg) VALUES ("Coating", 4, 1200);
INSERT INTO Stock ( Component, Conditionnementkg, Palettekg) VALUES ("Aroma", 4, 1200);
INSERT INTO Stock ( Component, Conditionnementkg, Palettekg) VALUES ("Gelling", 20, 1000);
INSERT INTO Stock ( Component, Conditionnementkg, Palettekg) VALUES ("Sugar", 20, 1000);
