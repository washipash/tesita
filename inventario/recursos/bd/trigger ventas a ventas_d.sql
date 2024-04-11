CREATE TRIGGER tr_insert_ventas_d
AFTER INSERT ON venta
FOR EACH ROW
BEGIN
    INSERT INTO ventas_d (ID_V, fecha, hora, precio_vent, prcio_bs)
    VALUES (NEW.ID_V, NEW.fecha, NEW.hora, NEW.precio_vent, NEW.prcio_bs);
END;