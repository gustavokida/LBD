package entidades;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.ManyToOne;

@Entity
public class Produto {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;
    private String descricao;
    private int qtd;
    private double valor;
    @ManyToOne
    private Categoria categoria;

    public Produto(int id) {
        this.id = id;
    }

    public Produto() {
    }

    public Produto(int id, String descricao, int qtd, double valor, Categoria categoria) {
        this.id = id;
        this.descricao = descricao;
        this.qtd = qtd;
        this.valor = valor;
        this.categoria = categoria;
    }
    
    public Produto(String descricao, int qtd, double valor, Categoria categoria) {
        this.descricao = descricao;
        this.qtd = qtd;
        this.valor = valor;
        this.categoria = categoria;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public int getQtd() {
        return qtd;
    }

    public void setQtd(int qtd) {
        this.qtd = qtd;
    }

    public double getValor() {
        return valor;
    }

    public void setValor(double valor) {
        this.valor = valor;
    }

    public Categoria getCategoria() {
        return categoria;
    }

    public void setCategoria(Categoria categoria) {
        this.categoria = categoria;
    }
    
    
}
