package co.edu.itm.taller.domain;

import co.edu.itm.taller.entities.Pedido;

import java.math.BigDecimal;

public class CostoEstandar implements ICalcularCosto {

    @Override
    public BigDecimal calcularCosto(Pedido pedido) {
        return new BigDecimal("3000");
    }

}
