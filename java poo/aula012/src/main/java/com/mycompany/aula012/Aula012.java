package com.mycompany.aula012;
public class Aula012 {
    public static void main(String[] args) {
        //Animal n = new Animal(); - abstrato
        Mamifero m = new Mamifero();
        Reptil r = new Reptil();
        Peixe p = new Peixe();
        Ave a = new Ave();
        Canguru c = new Canguru();
        Cachorro k = new Cachorro();
        Cobra j = new Cobra();
        Tartaruga t = new Tartaruga();
        Goldfish g = new Goldfish();
        Arara e = new Arara();
        
        //m.setNome("Joey");
        //System.out.println("Oi, " + m.getNome());
        
        m.setPeso(85.3f);
        m.setIdade(2);
        m.setMembros(4);
        m.alimentar();
        m.emitirSom();
        
        System.out.println("==================");
        m.locomover();
        r.locomover();
        p.locomover();
        a.locomover();
        System.out.println("==================");
        
        
       
    }
}
