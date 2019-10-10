-- A cada 10 compras o cliente ganha 50% de desconto;
-- Clientes vips recebem 10% de desconto do valor total em todas as compras.
CREATE OR REPLACE FUNCTION desconto()
RETURNS TRIGGER AS
$BODY$ 
DECLARE
    quantidade INTEGER;
    vip BOOLEAN;
BEGIN
    SELECT COUNT(*) INTO quantidade FROM compra WHERE NEW.idcliente = idcliente;
    IF quantidade % 10 = 9 THEN
        NEW.desconto = NEW.preco_total * 0.5;
    END IF;
    
    SELECT vip INTO vip FROM cliente where NEW.idcliente = cliente.idcliente;
    IF vip = true THEN
        NEW.desconto = NEW.desconto + NEW.preco_total * 0.1;
    END IF;
    
    NEW.preco_final = NEW.preco_total - NEW.desconto; 
    RETURN NEW;
END; 
$BODY$
LANGUAGE 'plpgsql';

DROP desconto ON Compra;
CREATE TRIGGER desconto_TG
BEFORE INSERT ON Compra
FOR EACH ROW
EXECUTE PROCEDURE desconto();


-- A partir de 5 unidades de um produto o cliente paga 50% em todas as unidades dele naquela compra;
CREATE OR REPLACE FUNCTION desconto_de_50_porcento_no_produto()
RETURNS TRIGGER AS
$BODY$ 
DECLARE
    quantidade INTEGER;
    valor INTEGER;
BEGIN
    quantidade := NEW.quantidade;
    IF quantidade >= 5 THEN
        SELECT valor INTO valor FROM midia WHERE NEW.idmidia = midia.idmidia;
        NEW.desconto_por_unidade = valor * 0.5;
    END IF;
    RETURN NEW;
END; 
$BODY$
LANGUAGE 'plpgsql';

DROP desconto_de_50_porcento_no_produto ON produtoscomprados;
CREATE TRIGGER desconto_de_50_porcento_no_produto_TG
BEFORE INSERT ON ProdutosComprados
FOR EACH ROW
EXECUTE PROCEDURE desconto_de_50_porcento_no_produto();


-- Depois de 100 compras o cliente vira vip;
CREATE OR REPLACE FUNCTION cliente_vira_vip_depois_de_100_compras()
RETURNS TRIGGER AS
$BODY$ 
DECLARE
    quantidade_de_compras INTEGER;
BEGIN
    SELECT COUNT(*) INTO quantidade_de_compras FROM compra WHERE NEW.idcliente = compra.idcliente;  
    IF quantidade_de_compras = 100 THEN
        UPDATE cliente SET vip = true where cliente = new.idcliente; 
    END IF;
    RETURN NEW;
END; 
$BODY$
LANGUAGE 'plpgsql';

DROP cliente_vira_vip_depois_de_100_compras ON produtoscomprados;
CREATE TRIGGER cliente_vira_vip_depois_de_100_compras
AFTER INSERT ON compra
FOR EACH ROW
EXECUTE PROCEDURE cliente_vira_vip_depois_de_100_compras();