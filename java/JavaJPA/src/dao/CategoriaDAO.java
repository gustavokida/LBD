package dao;

import entidades.Categoria;
import connection.ConnectionFactory;
import java.util.List;
import javax.persistence.EntityManager;

public class CategoriaDAO {
    public void save(Categoria c){
        EntityManager em = new ConnectionFactory().getConnection();
        try{
            em.getTransaction().begin();
            em.persist(c);
            em.getTransaction().commit();
        }catch(Exception ex){
            em.getTransaction().rollback();
        }finally{
            em.close();
        }
    }
    
    public void update(Categoria c){
        EntityManager em = new ConnectionFactory().getConnection();
        try{
            em.getTransaction().begin();
            em.merge(c);
            em.getTransaction().commit();
        }catch(Exception ex){
            em.getTransaction().rollback();
        }finally{
            em.close();
        }
    }
    
    public Categoria findById(int id){
        EntityManager em = new ConnectionFactory().getConnection();
        Categoria c = null;
        try{
            c = em.find(Categoria.class, id);
        }catch(Exception ex){
            System.err.println(ex);
        }finally{
            em.close();
        }
        return c;
    }
    
    public List<Categoria> findAll(){
        EntityManager em = new ConnectionFactory().getConnection();
        List<Categoria> categorias = null;
        try{
            categorias = em.createQuery("SELECT c FROM Categoria c").getResultList();
        }catch(Exception ex){
            System.err.println(ex);
        }finally{
            em.close();
        }
        return categorias;
    }
    
    public void remove(int id){
        EntityManager em = new ConnectionFactory().getConnection();
        try{
            Categoria c = em.find(Categoria.class, id);
            
            em.getTransaction().begin();
            em.remove(c);
            em.getTransaction().commit();
        }catch(Exception ex){
            em.getTransaction().rollback();
        }finally{
            em.close();
        }
    }
}
