package model.dao;

import connection.ConnectionFactory;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import model.bean.Categoria;
import model.bean.Produto;

public class ProdutoDAO {
    private Connection con = null;
    
    public ProdutoDAO() {
        con = ConnectionFactory.getConnection();
    }
    
    public boolean save(Produto produto){
        String sql = "INSERT INTO produto (descricao, qtd, valor, categoria_id) VALUES(?, ?, ?, ?)";
        
        PreparedStatement stmt = null;
        try {
            stmt = con.prepareStatement(sql);
            stmt.setString(1, produto.getDescricao());
            stmt.setInt(2, produto.getQtd());
            stmt.setDouble(3, produto.getValor());
            stmt.setInt(4, produto.getCategoria().getId());
            stmt.executeUpdate();
            return true;
        } catch (SQLException ex) {
            System.err.println("Erro: " + ex);
            return false;
        }finally{
            ConnectionFactory.closeConnection(con, stmt);
        }
    }
    
    public List<Produto> findAll(){
        String sql = "SELECT * FROM produto p INNER JOIN categoria c ON p.categoria_id = c.id";
        
        PreparedStatement stmt = null;
        ResultSet rs = null;
        
        List<Produto> produtos = new ArrayList<>();
        
        try {
            stmt = con.prepareStatement(sql);
            rs = stmt.executeQuery();
            
            while(rs.next()){
                Categoria c = new Categoria(rs.getInt("categoria_id"), rs.getString("c.descricao"));
                
                Produto p = new Produto();
                p.setId(rs.getInt("id"));
                p.setDescricao(rs.getString("p.descricao"));
                p.setQtd(rs.getInt("qtd"));
                p.setValor(rs.getDouble("valor"));
                p.setCategoria(c);
                
                produtos.add(p);
            }
        } catch (SQLException ex) {
            System.err.println("Erro: " + ex);
        }finally{
            ConnectionFactory.closeConnection(con, stmt, rs);
        }
        return produtos;
    } 
    
    public boolean update(Produto p){
        String sql = "UPDATE produto set descricao = ?, qtd = ?, valor = ?, categoria_id = ? WHERE id = ?";
        
        PreparedStatement stmt = null;
        try {
            stmt = con.prepareStatement(sql);
            stmt.setString(1, p.getDescricao());
            stmt.setInt(2, p.getQtd());
            stmt.setDouble(3, p.getValor());
            stmt.setInt(4, p.getCategoria().getId());
            stmt.setInt(5, p.getId());
            stmt.executeUpdate();
            return true;
        } catch (SQLException ex) {
            System.err.println("Erro: " + ex);
            return false;
        }finally{
            ConnectionFactory.closeConnection(con, stmt);
        }
    }
    
    public boolean delete(Produto p){
        String sql = "DELETE FROM produto WHERE id = ?";
        
        PreparedStatement stmt = null;
        try {
            stmt = con.prepareStatement(sql);
            stmt.setInt(1, p.getId());
            stmt.executeUpdate();
            return true;
        } catch (SQLException ex) {
            System.err.println("Erro: " + ex);
            return false;
        }finally{
            ConnectionFactory.closeConnection(con, stmt);
        }
    }
    
}
