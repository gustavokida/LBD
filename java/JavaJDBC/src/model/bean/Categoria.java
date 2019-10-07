package model.bean;

public class Categoria {
    private int id;
    private String descricao;

    public Categoria(int id) {
        this.id = id;
    }

    public Categoria(String descricao) {
        this.descricao = descricao;
    }

    public Categoria(int id, String descricao) {
        this.id = id;
        this.descricao = descricao;
    }
    
    public Categoria() {
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
    
    
}
