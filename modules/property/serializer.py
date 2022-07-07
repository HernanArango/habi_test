
class PropertySerializer:
    @staticmethod
    def to_dict(data):
        property_list = []
        for property_fields in data:
            property_dict = {
                # "id": property_fields[0],
                "address": property_fields[1],
                "city": property_fields[2],
                "price": property_fields[3],
                "description": property_fields[4],
                # "year": property_fields[5],
                "actual_state": property_fields[6]

            }
            property_list.append(property_dict)

        return property_list
