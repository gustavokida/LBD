package connection;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;

public class ConnectionFactory {

    private static final EntityManagerFactory emf = Persistence.createEntityManagerFactory("meuPU");

    public EntityManager getConnection() {
        return emf.createEntityManager();
    }
    
    public void closeConnection(){
        emf.close();
    }
    
}