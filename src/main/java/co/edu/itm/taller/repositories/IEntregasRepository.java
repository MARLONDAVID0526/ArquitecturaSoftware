package co.edu.itm.taller.repositories;

import co.edu.itm.taller.entities.Entregas;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.UUID;

@Repository
public interface IEntregasRepository extends JpaRepository<Entregas, UUID> {

}
