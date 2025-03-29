package co.edu.itm.taller.entities;

import co.edu.itm.taller.entities.enumerators.TipoTransportista;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;
import java.util.UUID;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class Transportista {

    private UUID id;
    private String nombre;
    private int capacidad;
    private List<Pedido> pedidosAsignados;
    private TipoTransportista tipo;

    private void validarCapacidadMaxima() {
        if (TipoTransportista.EXTERNO.equals(this.tipo))
                capacidad = 10;
        else
            capacidad = 20;
    }

}
