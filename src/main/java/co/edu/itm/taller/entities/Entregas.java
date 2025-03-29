package co.edu.itm.taller.entities;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.UUID;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class Entregas {

    private UUID id;
    private UUID idTransportista;
    private UUID idPedido;

}
