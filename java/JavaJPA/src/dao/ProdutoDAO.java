package dao;

import connection.ConnectionFactory;
import entidades.Produto;
import java.util.List;
import javax.persistence.EntityManager;

public class ProdutoDAO {
    public Produto save(Produto p){
        EntityManager em = new ConnectionFactory().getConnection();
        try{
            em.getTransaction().begin();
            em.persist(p);
            em.getTransaction().commit();
        }catch(Exception e){
            em.getTransaction().rollback();
        }finally{
            em.close();
        }
        return p;
    }
    
    public void update(Produto p){
        EntityManager em = new ConnectionFactory().getConnection();
        try{
            em.getTransaction().begin();
            em.merge(p);
            em.getTransaction().commit();
        }catch(Exception ex){
            em.getTransaction().rollback();
        }finally{
            em.close();
        }
    }
    
    public Produto findById(int id){
        EntityManager em = new ConnectionFactory().getConnection();
        Produto p = null;
        try{
            p = em.find(Produto.class, id);
        }catch(Exception ex){
            System.err.println(ex);
        }finally{
            em.close();
        }
        return p;
    }
    
    public List<Produto> findAll(){
        EntityManager em = new ConnectionFactory().getConnection();
        List<Produto> produtos = null;
        try{
            produtos = em.createQuery("SELECT p FROM Produto p").getResultList();
        }catch(Exception ex){
            System.err.println(ex);
        }finally{
            em.close();
        }
        return produtos;
    }
    
    public void remove(int id){
        EntityManager em = new ConnectionFactory().getConnection();
        try{
            Produto p = em.find(Produto.class, id);
            
            em.getTransaction().begin();
            em.remove(p);
            em.getTransaction().commit();
        }catch(Exception ex){
            em.getTransaction().rollback();
        }finally{
            em.close();
        }
    }
}