package connection;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class ConnectionFactory {
    private static String DRIVER = "com.mysql.jdbc.Driver";
    private static String URL = "jdbc:mysql://localhost:3306/dbloja";
    private static String USER = "root";
    private static String PASSWORD = "";

    public static Connection getConnection(){
        try{
            Class.forName(DRIVER);
            return DriverManager.getConnection(URL, USER, PASSWORD);
        }catch(Exception ex){
            System.err.println("Erro: " + ex);
            return null;
        }
    }
    
    public static void closeConnection(Connection con){
        if (con != null) {
            try{
                con.close();
            }catch(SQLException ex){
                System.err.println("Erro: " + ex);
            }
        }
    }
     
    public static void closeConnection(Connection con, PreparedStatement stmt){
        if (stmt != null) {
            try{
                stmt.close();
            }catch(SQLException ex){
                System.err.println("Erro: " + ex);
            }
        }
        
        closeConnection(con);
    }
     
    public static void closeConnection(Connection con, PreparedStatement stmt, ResultSet rs){
        if (rs != null) {
            try{
                rs.close();
            }catch(SQLException ex){
                System.err.println("Erro: " + ex);
            }
        }
        
        closeConnection(con, stmt);
    }
    
}
