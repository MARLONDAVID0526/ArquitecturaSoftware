package co.edu.itm.taller.services;

import co.edu.itm.taller.domain.IOperacionesPedido;
import co.edu.itm.taller.domain.OperacionesPedido;
import co.edu.itm.taller.entities.Pedido;
import co.edu.itm.taller.entities.Transportista;
import co.edu.itm.taller.repositories.IPedidosRepository;
import co.edu.itm.taller.repositories.ITransportistaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.rmi.server.UID;
import java.util.UUID;

@Service
public class PedidosService {

    @Autowired
    private IPedidosRepository pedidosRepository;

    @Autowired
    private ITransportistaRepository transportistaRepository;

    private IOperacionesPedido operacionesPedido;

    public void crearPedido(Pedido pedido) {
        pedidosRepository.save(pedido);
    }

    public  void consultarPedido(Pedido pedido) {
        pedidosRepository.findById(pedido.getId());
    }

    public BigDecimal calcularCostoEnvio(Pedido pedido) {
        return pedido.calcularCostoEnvio();
    }

    public void actualizarPedido(Pedido pedido) {
        pedidosRepository.save(pedido);
    }

    public void cancelarPedido(Pedido pedido) {
        pedidosRepository.delete(pedido);
    }

    public void asignarTransportista(Transportista transportista, Pedido pedido) {
        operacionesPedido = new OperacionesPedido();
        operacionesPedido.asignarTrasportista(transportista, pedido);
    }

}
