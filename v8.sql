DROP TABLE IF EXISTS ProdutosComprados;
DROP TABLE IF EXISTS Compra;
DROP TABLE IF EXISTS Funcionario;
DROP TABLE IF EXISTS Cliente;
DROP TABLE IF EXISTS Midia;
DROP TABLE IF EXISTS Genero;
DROP TABLE IF EXISTS Livro;
DROP TABLE IF EXISTS Manga;
DROP TABLE IF EXISTS Volume;
DROP TABLE IF EXISTS Revista;
DROP TABLE IF EXISTS Autor;

CREATE TABLE public.Genero (
                IdGenero SERIAL,
                Nome VARCHAR NOT NULL,
                Localizacao VARCHAR NOT NULL,
                CONSTRAINT genero_pk PRIMARY KEY (IdGenero)
);


CREATE TABLE public.Livro (
                IdLivro SERIAL,
                Sinopse VARCHAR NOT NULL,
                Titulo_do_Livro VARCHAR NOT NULL,
                Edicao INTEGER NOT NULL CHECK(Edicao > 0),
                Paginas INTEGER NOT NULL CHECK(Paginas > 0),
                CONSTRAINT livro_pk PRIMARY KEY (IdLivro)
);


CREATE TABLE public.Volume (
                IdVolume SERIAL,
                Sinopse VARCHAR NOT NULL,
                Numero INTEGER NOT NULL CHECK(Numero > 0),
                Nome VARCHAR NOT NULL,
                CONSTRAINT volume_pk PRIMARY KEY (IdVolume)
);


CREATE TABLE public.Manga (
                IdManga SERIAL,
                IdVolume INTEGER NOT NULL,
                Capitulo INTEGER NOT NULL CHECK(Capitulo > 0),
                Titulo_do_Capitulo VARCHAR NOT NULL,
                CONSTRAINT manga_pk PRIMARY KEY (IdManga)
);


CREATE TABLE public.Revista (
                IdRevista SERIAL,
                Empresa VARCHAR NOT NULL,
                Edicao INTEGER NOT NULL CHECK(Edicao > 0),
                CONSTRAINT revista_pk PRIMARY KEY (IdRevista)
);


CREATE TABLE public.Autor (
                IdAutor SERIAL,
                Nacionalidade VARCHAR NOT NULL,
                Nome VARCHAR NOT NULL,
                Data_de_Nascimento DATE NOT NULL,
                Data_de_Falecimento DATE NOT NULL,
                CHECK (Data_de_Falecimento > Data_de_Nascimento),
                CONSTRAINT autor_pk PRIMARY KEY (IdAutor)
);


CREATE TABLE public.Midia (
                IdMidia SERIAL,
                IdManga INTEGER,
                IdLivro INTEGER,
                IdRevista INTEGER,
                IdGenero INTEGER NOT NULL,
                IdAutor INTEGER NOT NULL,
                Data_de_Publicacao DATE NOT NULL,
                Editora VARCHAR NOT NULL,
                Nome VARCHAR NOT NULL,
                Idioma VARCHAR NOT NULL,
                Local_de_Publicacao VARCHAR NOT NULL,
                Valor FLOAT NOT NULL CHECK(Valor > 0),
                CONSTRAINT midia_pk PRIMARY KEY (IdMidia)
);


CREATE TABLE public.Funcionario (
                IdFuncionario SERIAL,
                Funcao VARCHAR NOT NULL,
                Nome VARCHAR NOT NULL,
                Salario FLOAT NOT NULL CHECK(Salario > 0),
                Data_Admissao DATE NOT NULL,
                CONSTRAINT funcionario_pk PRIMARY KEY (IdFuncionario)
);


CREATE TABLE public.Cliente (
                IdCliente SERIAL,
                Endereco VARCHAR NOT NULL,
                Sexo VARCHAR NOT NULL,
                Nome VARCHAR NOT NULL,
                Data_de_Nascimento DATE NOT NULL,
                Vip BOOLEAN NOT NULL,
                CONSTRAINT cliente_pk PRIMARY KEY (IdCliente)
);


CREATE TABLE public.Compra (
                IdCompra SERIAL,
                IdFuncionario INTEGER NOT NULL,
                IdCliente INTEGER NOT NULL,
                Data DATE NOT NULL,
                Preco_Total FLOAT NOT NULL CHECK(Preco_Total > 0),
                Desconto FLOAT NOT NULL CHECK(Desconto > 0),
                Preco_Final FLOAT NOT NULL CHECK(Preco_Final > 0),
                CONSTRAINT compra_pk PRIMARY KEY (IdCompra)
);


CREATE TABLE public.ProdutosComprados (
                IdProdutosComprados SERIAL,
                IdCompra INTEGER NOT NULL,
                IdMidia INTEGER NOT NULL,
                Quantidade INTEGER NOT NULL CHECK(Quantidade > 0),
                CONSTRAINT produtoscomprados_pk PRIMARY KEY (IdProdutosComprados)
);


ALTER TABLE public.Midia ADD CONSTRAINT genero_midia_fk
FOREIGN KEY (IdGenero)
REFERENCES public.Genero (IdGenero)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.Midia ADD CONSTRAINT livro_midia_fk
FOREIGN KEY (IdLivro)
REFERENCES public.Livro (IdLivro)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.Manga ADD CONSTRAINT volume_manga_fk
FOREIGN KEY (IdVolume)
REFERENCES public.Volume (IdVolume)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.Midia ADD CONSTRAINT manga_midia_fk
FOREIGN KEY (IdManga)
REFERENCES public.Manga (IdManga)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.Midia ADD CONSTRAINT revista_midia_fk
FOREIGN KEY (IdRevista)
REFERENCES public.Revista (IdRevista)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.Midia ADD CONSTRAINT autor_midia_fk
FOREIGN KEY (IdAutor)
REFERENCES public.Autor (IdAutor)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.ProdutosComprados ADD CONSTRAINT midia_produtoscomprados_fk
FOREIGN KEY (IdMidia)
REFERENCES public.Midia (IdMidia)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.Compra ADD CONSTRAINT funcionario_compra_fk
FOREIGN KEY (IdFuncionario)
REFERENCES public.Funcionario (IdFuncionario)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.Compra ADD CONSTRAINT cliente_compra_fk
FOREIGN KEY (IdCliente)
REFERENCES public.Cliente (IdCliente)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.ProdutosComprados ADD CONSTRAINT compra_produtoscomprados_fk
FOREIGN KEY (IdCompra)
REFERENCES public.Compra (IdCompra)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;