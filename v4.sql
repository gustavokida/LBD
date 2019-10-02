/* v4: */

CREATE TABLE Cliente (
    Endereco VARCHAR,
    Sexo VARCHAR,
    ID INTEGER PRIMARY KEY,
    Nome VARCHAR,
    Data_de_Nascimento DATE
);

CREATE TABLE Funcionario (
    ID INTEGER PRIMARY KEY,
    Funcao VARCHAR,
    Nome VARCHAR,
    Salario FLOAT,
    Data_de_Admissao DATE
);

CREATE TABLE Autor (
    ID INTEGER PRIMARY KEY,
    Nacionalidade VARCHAR,
    Nome VARCHAR,
    Data_Nascimento DATE,
    Data_Falecimento DATE
);

CREATE TABLE Genero (
    ID INTEGER PRIMARY KEY,
    Nome VARCHAR,
    Localizacao VARCHAR
);

CREATE TABLE Manga (
    ID INTEGER PRIMARY KEY,
    Capitulo INTEGER,
    fk_Volume_ID INTEGER,
    Titulo_do_Capitulo VARCHAR
);

CREATE TABLE Livro (
    Nome_do_Volume VARCHAR,
    Sinopse VARCHAR,
    ID INTEGER PRIMARY KEY,
    Titulo_do_Livro VARCHAR
);

CREATE TABLE Volume (
    Sinopse VARCHAR,
    Numero INTEGER,
    Nome VARCHAR,
    ID INTEGER PRIMARY KEY
);

CREATE TABLE Revista (
    Empresa VARCHAR,
    Edicao INTEGER,
    ID INTEGER PRIMARY KEY
);

CREATE TABLE Produtos_Comprados (
    ID INTEGER PRIMARY KEY,
    fk_Compra_ID INTEGER,
    fk_Midia_ID INTEGER
);

CREATE TABLE Compra (
    Data DATE,
    Preco_Total FLOAT,
    Desconto FLOAT,
    Preco_Final FLOAT,
    ID INTEGER PRIMARY KEY,
    ClienteID INTEGER,
    fk_Funcionario_ID INTEGER
);

CREATE TABLE Midia (
    ID INTEGER PRIMARY KEY,
    Data_de_Publicacao INTEGER,
    Editora INTEGER,
    Nome VARCHAR,
    Idioma INTEGER,
    Local_de_Publicacao VARCHAR,
    fk_Genero_ID INTEGER,
    fk_Autor_ID INTEGER,
    fk_Revista_ID INTEGER,
    fk_Manga_ID INTEGER,
    fk_Livro_ID INTEGER
);
 
ALTER TABLE Compra ADD CONSTRAINT FK_Compra_1
    FOREIGN KEY (ClienteID)
    REFERENCES Cliente (ID);
 
ALTER TABLE Compra ADD CONSTRAINT FK_Compra_2
    FOREIGN KEY (fk_Funcionario_ID)
    REFERENCES Funcionario (ID);
 
ALTER TABLE Produtos_Comprados ADD CONSTRAINT FK_Produtos_Comprados_1
    FOREIGN KEY (fk_Compra_ID)
    REFERENCES Compra (ID);

ALTER TABLE Produtos_Comprados ADD CONSTRAINT FK_Produtos_Comprados_2
    FOREIGN KEY (fk_Midia_ID)
    REFERENCES Midia (ID);
 
ALTER TABLE Midia ADD CONSTRAINT FK_Midia_1
    FOREIGN KEY (fk_Genero_ID)
    REFERENCES Genero (ID);
 
ALTER TABLE Midia ADD CONSTRAINT FK_Midia_2
    FOREIGN KEY (fk_Autor_ID)
    REFERENCES Autor (ID);
 
ALTER TABLE Midia ADD CONSTRAINT FK_Midia_3
    FOREIGN KEY (fk_Revista_ID)
    REFERENCES Revista (ID);

ALTER TABLE Midia ADD CONSTRAINT FK_Midia_4
    FOREIGN KEY (fk_Manga_ID)
    REFERENCES Manga (ID);    

ALTER TABLE Midia ADD CONSTRAINT FK_Midia_5
    FOREIGN KEY (fk_Livro_ID)
    REFERENCES Livro (ID);    
 
ALTER TABLE Manga ADD CONSTRAINT FK_Manga_1
    FOREIGN KEY (fk_Volume_ID)
    REFERENCES Volume (ID);