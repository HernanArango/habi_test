from db import DB as db
from modules.property.serializer import PropertySerializer


def get_properties():
    sql = """
        select * 
        from(
            select 
                p.id,
                p.address,
                p.city,
                p.price,
                p.description,
                (
                    select 
                        s.name
                    from 
                        status_history sh
                    join 
                        status s on s.id=status_id
                    where 
                        sh.property_id=p.id
                        order by sh.id desc limit 1
                ) as actual_state
            from 
                property  p
        ) as tmp 
        where 
            tmp.actual_state='pre_venta' or tmp.actual_state='en_venta' or tmp.actual_state='vendido' limit 10
        """

    result = db.query(sql)
    return PropertySerializer.to_dict(result)
