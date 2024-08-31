import com.mycompany.projetolivro.Livro;
import com.mycompany.projetolivro.Pessoa;
public class ProjetoLivro {
    public static void main(String[] args) {
        Pessoa[] p = new Pessoa[2]; 
        Livro[] l = new Livro[3];
        
        p[0] = new Pessoa("Pedro", 22, "M");
        p[1] = new Pessoa("Maria", 25,  "F");
        
        l[0] = new Livro("Hipotese do Amor", "Ali hazelwood", 389, p[1]);
        l[1] = new Livro("Percy Jackson", "Rick Riordan", 306, p[0]);
        l[2] = new Livro("Hearstopper", "Alice Olseman", 234, p[1]);
        
        System.out.println(l[0].detalhes());
    }
}
