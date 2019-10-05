CREATE TABLE Autor (
    ID SERIAL PRIMARY KEY NOT NULL,
    Nacionalidade VARCHAR NOT NULL,
    Nome VARCHAR NOT NULL,
    Data_de_Nascimento DATE NOT NULL,
    Data_de_Falecimento DATE NOT NULL
);

CREATE TABLE Cliente (
    Endereco VARCHAR NOT NULL,
    Sexo VARCHAR NOT NULL,
    ID SERIAL PRIMARY KEY NOT NULL,
    Nome VARCHAR NOT NULL,
    Data_de_Nascimento DATE NOT NULL
);

CREATE TABLE Compra (
    Data DATE NOT NULL,
    Preco_Total FLOAT NOT NULL,
    Desconto FLOAT NOT NULL,
    Preco_Final FLOAT NOT NULL,
    ID SERIAL PRIMARY KEY NOT NULL,
    fk_Cliente_ID INTEGER NOT NULL,
    fk_Funcionario_ID INTEGER NOT NULL
);

CREATE TABLE Funcionario (
    ID SERIAL PRIMARY KEY NOT NULL,
    Funcao VARCHAR NOT NULL,
    Nome VARCHAR NOT NULL,
    Salario FLOAT NOT NULL,
    Data_de_Admissao DATE NOT NULL
);

CREATE TABLE Genero (
    ID SERIAL PRIMARY KEY NOT NULL,
    Nome VARCHAR NOT NULL,
    Localizacao VARCHAR NOT NULL
);

CREATE TABLE Livro (
    Nome_do_Volume VARCHAR NOT NULL,
    Sinopse VARCHAR NOT NULL,
    ID SERIAL PRIMARY KEY NOT NULL,
    Titulo_do_Livro VARCHAR NOT NULL
);

CREATE TABLE Manga (
    ID SERIAL PRIMARY KEY NOT NULL,
    Capitulo INTEGER NOT NULL,
    fk_Volume_ID INTEGER NOT NULL,
    Titulo_do_Capitulo VARCHAR NOT NULL
);

CREATE TABLE Midia (
    ID SERIAL PRIMARY KEY NOT NULL,
    Data_de_Publicacao DATE NOT NULL,
    Editora VARCHAR NOT NULL,
    Nome VARCHAR NOT NULL,
    Idioma VARCHAR NOT NULL,
    Local_de_Publicacao VARCHAR NOT NULL,
    fk_Genero_ID INTEGER NOT NULL,
    fk_Autor_ID INTEGER NOT NULL,
    fk_Revista_ID INTEGER NOT NULL,
    fk_Manga_ID INTEGER NOT NULL,
    fk_Livro_ID INTEGER NOT NULL
);

CREATE TABLE Produtos_Comprados (
    ID SERIAL PRIMARY KEY NOT NULL,
    fk_Compra_ID INTEGER NOT NULL,
    fk_Midia_ID INTEGER NOT NULL
);

CREATE TABLE Revista (
    Empresa VARCHAR NOT NULL,
    Edicao INTEGER NOT NULL,
    ID SERIAL PRIMARY KEY NOT NULL
);

CREATE TABLE Volume (
    Sinopse VARCHAR NOT NULL,
    Numero INTEGER NOT NULL,
    Nome VARCHAR NOT NULL,
    ID SERIAL PRIMARY KEY NOT NULL
);
 
ALTER TABLE Compra ADD CONSTRAINT FK_Compra_1
    FOREIGN KEY (fk_Cliente_ID)
    REFERENCES Cliente (ID);
 
ALTER TABLE Compra ADD CONSTRAINT FK_Compra_2
    FOREIGN KEY (fk_Funcionario_ID)
    REFERENCES Funcionario (ID);   
 
ALTER TABLE Manga ADD CONSTRAINT FK_Manga_1
    FOREIGN KEY (fk_Volume_ID)
    REFERENCES Volume (ID);
 
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
 
ALTER TABLE Produtos_Comprados ADD CONSTRAINT FK_Produtos_Comprados_1
    FOREIGN KEY (fk_Compra_ID)
    REFERENCES Compra (ID);
    
ALTER TABLE Produtos_Comprados ADD CONSTRAINT FK_Produtos_Comprados_2
    FOREIGN KEY (fk_Midia_ID)
    REFERENCES Midia (ID);