package co.edu.itm.taller.domain;

import co.edu.itm.taller.entities.Pedido;
import co.edu.itm.taller.entities.Transportista;

public interface IOperacionesPedido {

    void asignarTrasportista(Transportista transportista, Pedido pedido);

    void actualizarPedido(Pedido pedido);

}
