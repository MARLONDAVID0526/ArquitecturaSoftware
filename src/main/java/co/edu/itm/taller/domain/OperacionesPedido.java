package co.edu.itm.taller.domain;

import co.edu.itm.taller.entities.Pedido;
import co.edu.itm.taller.entities.Transportista;
import org.springframework.stereotype.Component;

@Component
public class OperacionesPedido implements IOperacionesPedido {

    @Override
    public void asignarTrasportista(Transportista transportista, Pedido pedido) {

    }

    @Override
    public void actualizarPedido(Pedido pedido) {
        
    }

}
