package model.dao;

import model.bean.Categoria;
import model.bean.Produto;
import org.junit.Test;
import static org.junit.Assert.*;
import org.junit.Ignore;

public class ProdutoDAOTest {
    
    public ProdutoDAOTest() {
    }

    @Test
    public void inserir() {
        Categoria c = new Categoria(3);        
        Produto p = new Produto("Bolacha", 2, 2, c);
        
        ProdutoDAO dao = new ProdutoDAO();
        if(dao.save(p)){
            System.out.println("Sucesso ao inserir!");
        }else{
            fail("Falha ao inserir!");
        }
    }
    
    @Test
    public void atualizar() {
        Categoria c = new Categoria(3);        
        Produto p = new Produto(5, "Biscoito", 2, 2, c);
        
        ProdutoDAO dao = new ProdutoDAO();
        if(dao.update(p)){
            System.out.println("Atualizado com sucesso!");
        }else{
            fail("Erro ao atualizar!");
        }
    }

    @Test
    public void deletar() {
        Categoria c = new Categoria();
        Produto p = new Produto(5, "Alimentos", 3, 5.0, c);
        
        ProdutoDAO dao = new ProdutoDAO();
        if(dao.delete(p)){
            System.out.println("Deletado com sucesso!");
        }else{
            fail("Erro ao deletar!");
        }
    }


    @Test
    public void listar(){
        ProdutoDAO dao = new ProdutoDAO();
        for(Produto p: dao.findAll()){
            System.out.println("Id : " + p.getId());
            System.out.println(" - Descrição: " + p.getDescricao());
            System.out.println(" - Quantidade: " + p.getQtd());
            System.out.println(" - Valor: " + p.getValor());
            System.out.println(" - Id_categoria: " + p.getCategoria().getId());
            System.out.println(" - Categoria: " + p.getCategoria().getDescricao());
        }
    }
    
}
