package src;

import javax.jws.WebMethod;
import javax.jws.WebService;
import javax.xml.ws.Endpoint;
import javax.xml.ws.WebServiceRef;
import java.util.*;

/**
 * Created by forte on 06/07/16.
 */
@WebService()
public class ServicioEstudiante {
    private static Map<Integer,Estudiante> estudiantes;

    static {
        estudiantes = new HashMap<>();
    }

    @WebMethod
    public Estudiante crearEstudiante(Estudiante e) {
        //agregando instancia de nuevo estudiantes al "listado"
        estudiantes.put(e.getMatricula(),e);

        return e;
    }

    @WebMethod
    public Estudiante modificarEstudiante(Estudiante target) {
        if(estudiantes.containsKey(target.getMatricula())) {
            //reemplazando viejos valores en la lista
            estudiantes.replace(target.getMatricula(),target);

            //retornar el mismo estudiante que se trato de modificar
            return target;
        }
        else {

            //retornar null si el estudiante no esta agregado en la lista
            return null;
        }
    }

    @WebMethod
    public void eliminarEstudiante(Integer target) {
        if(estudiantes.containsKey(target.intValue())) {
            estudiantes.remove(target.intValue());
        }
    }

    @WebMethod
    public Estudiante obtenerEstudiante(Integer matricula) {
        return estudiantes.get(matricula);
    }

    @WebMethod
    public Estudiante[] listarEstudiantes() {
        return estudiantes.values().toArray(new Estudiante[estudiantes.size()]);
    }

    public static void main(String[] argv) {
        Object implementor = new ServicioEstudiante();
        Endpoint.publish("http://localhost:9001/ServicioEstudiante", implementor);
    }
}
