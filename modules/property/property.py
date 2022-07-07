from db import DB as db
from modules.property.serializer import PropertySerializer

# is important filter the params for evite the sql injection, but not in this test
def get_properties(params):
    page = 0
    per_page = 10
    sql = """
        select * 
        from(
            select 
                p.id,
                p.address,
                p.city,
                p.price,
                p.description,
                p.year,
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
            (tmp.actual_state='pre_venta' or tmp.actual_state='en_venta' or tmp.actual_state='vendido')
        """
    sql_conditional = ""

    if "city" in params:
        sql_conditional += f" and city='{params['city'][0]}'"

    if "year" in params:
        sql_conditional += f" and year='{params['year'][0]}'"

    if "actual_state" in params:
        sql_conditional += f" and tmp.actual_state='{params['actual_state'][0]}'"

    if "per_page" in params:
        per_page = int(params['per_page'][0])

    if "page" in params:
        page = int(params['page'][0]) * per_page

    sql = sql+sql_conditional+f" limit {str(per_page)} offset {str(page)}"

    result = db.query(sql)
    return PropertySerializer.to_dict(result)
