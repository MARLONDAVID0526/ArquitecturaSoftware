package co.edu.itm.taller.domain;

import co.edu.itm.taller.entities.Pedido;
import co.edu.itm.taller.entities.enumerators.TipoEnvio;

import java.math.BigDecimal;

public interface ICalcularCosto {

    BigDecimal calcularCosto(Pedido pedido);

}
