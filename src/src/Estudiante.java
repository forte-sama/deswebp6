package src;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by forte on 06/07/16.
 */
public class Estudiante {
    private Integer matricula;
    private String nombre;
    private String carrera;
    private List<Asignatura> asignaturas;


    public Estudiante() {
        Asignatura a1 = new Asignatura();
        a1.setCodigo("ISC-434");
        a1.setNombre("Ing Soft");

//        asignaturas.add(a1);
        asignaturas = new ArrayList<>();
    }


    public List<Asignatura> getAsignaturas() {
        return asignaturas;
    }

    public void setAsignaturas(List<Asignatura> asignaturas) {
        this.asignaturas = asignaturas;
    }

    public Integer getMatricula() {
        return matricula;
    }

    public void setMatricula(Integer matricula) {
        this.matricula = matricula;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getCarrera() {
        return carrera;
    }

    public void setCarrera(String carrera) {
        this.carrera = carrera;
    }

    @Override
    public String toString() {
        String str = this.getMatricula() + " : " + this.getNombre() + " : " + this.getCarrera() + "\nAsignaturas:\n";

//        for(Asignatura a : asignaturas) {
//            str += "\t" + a.getCodigo() + " : " + a.getNombre() + "\n";
//        }

        return str;
    }
}
