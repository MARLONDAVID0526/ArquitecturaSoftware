package co.edu.itm.taller.services;

import co.edu.itm.taller.domain.IOperacionesPedido;
import co.edu.itm.taller.domain.OperacionesPedido;
import co.edu.itm.taller.entities.Entregas;
import co.edu.itm.taller.entities.Pedido;
import co.edu.itm.taller.repositories.IEntregasRepository;
import co.edu.itm.taller.repositories.IPedidosRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

@Service
public class TransportistaService {

    IOperacionesPedido operacionesPedido;

    @Autowired
    IEntregasRepository entregasRepository;

    @Autowired
    IPedidosRepository pedidosRepository;

    public TransportistaService(IOperacionesPedido operacionesPedido) {
        this.operacionesPedido = operacionesPedido;
    }

    public List<Pedido> consultarEntregas() {
        List<Entregas> entregas = entregasRepository.findAll();
        return entregas.stream().flatMap(entrega ->
                pedidosRepository.findById(entrega.getId()).stream()).toList();
    }

    public void actualizarPedido(Pedido pedido) {
        pedidosRepository.save(pedido);
    }
}
