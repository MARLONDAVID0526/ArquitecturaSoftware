package co.edu.itm.taller.entities;

import co.edu.itm.taller.domain.CostoEstandar;
import co.edu.itm.taller.domain.CostoExpress;
import co.edu.itm.taller.domain.CostoProgramado;
import co.edu.itm.taller.domain.ICalcularCosto;
import co.edu.itm.taller.entities.enumerators.Estado;
import co.edu.itm.taller.entities.enumerators.TipoEnvio;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.math.BigDecimal;
import java.util.UUID;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class Pedido {

    private UUID id;
    private String direccionEntrega;
    private Estado estado;
    private TipoEnvio tipoEnvio;

    public BigDecimal calcularCostoEnvio(){
        ICalcularCosto calcularCosto = null;
        BigDecimal costo;
        switch (tipoEnvio) {
            case EXPRESS -> calcularCosto = new CostoExpress();
            case ESTANDAR -> calcularCosto = new CostoEstandar();
            case PROGRAMADA -> calcularCosto = new CostoProgramado();
        }
        costo = calcularCosto.calcularCosto(this);
        return costo;
    }

}
