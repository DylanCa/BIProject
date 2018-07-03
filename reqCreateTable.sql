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
	Quantity INT
);

CREATE TABLE Country (
	Id INT PRIMARY KEY NOT NULL,
	Name VARCHAR(50),
	FOREIGN KEY (Id) REFERENCES Packaging(Id)
);

CREATE TABLE Machine (
	Id INT PRIMARY KEY NOT NULL,
	Num INT,
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

CREATE TABLE CandyReferences (
	FOREIGN KEY (Id) REFERENCES Candy(Id),
	FOREIGN KEY (Id) REFERENCES Color(Id),
	FOREIGN KEY (Id) REFERENCES Texture(Id),
	FOREIGN KEY (Id) REFERENCES Variant(Id),
	FOREIGN KEY (Id) REFERENCES Packaging(Id)
);

CREATE TABLE Order (
	Id INT PRIMARY KEY NOT NULL,
	ClientName VARCHAR(50),
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

CREATE TABLE Stock (
	Id INT PRIMARY KEY NOT NULL,
	Component VARCHAR(10),
	Conditionnement(kg) INT,
	Palette(kg) INT
);