package model.dao;

import model.bean.Categoria;
import org.junit.Test;
import static org.junit.Assert.*;

public class CategoriaDAOTest {
    @Test
    public void inserir() {
        Categoria categoria = new Categoria("Roupas");
        CategoriaDAO dao = new CategoriaDAO();
        if(dao.save(categoria)){
            System.out.println("Salvo com sucesso!");
        }else{
            fail("Erro ao salvar!");
        }
    }
    
    @Test
    public void atualizar() {
        Categoria categoria = new Categoria("Comidas");
        CategoriaDAO dao = new CategoriaDAO();
        if(dao.update(categoria)){
            System.out.println("Atualizado com sucesso!");
        }else{
            fail("Erro ao atualizar!");
        }
    }

    @Test
    public void deletar() {
        Categoria categoria = new Categoria(1);
        CategoriaDAO dao = new CategoriaDAO();
        if(dao.delete(categoria)){
            System.out.println("Deletado com sucesso!");
        }else{
            fail("Erro ao deletar!");
        }
    }
    
    @Test
    public void listar(){
        CategoriaDAO dao = new CategoriaDAO();
        for(Categoria c: dao.findAll()){
            System.out.println("Descrição: " + c.getDescricao());
        }
    }
    
}
