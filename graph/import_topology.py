import pandas as pd
from pathlib import Path
from neo4j_client import driver

BASE_DIR = Path(__file__).resolve().parent.parent

FILE = BASE_DIR / "data" / "Topology Master_updated.xlsx"


def import_locations():

    print("Importing Locations...")

    df = pd.read_excel(
        FILE,
        sheet_name="Location"
    )

    with driver.session() as session:

        for _, row in df.iterrows():

            district = str(row["District"]).strip()
            mandal = str(row["Mandal"]).strip()
            lgd_code = str(row["LGD Code"]).strip()

            location_name = str(row["Location Name"]).strip()
            location_type = str(row["Type of Location"]).strip()

            latitude = row["LATITUDE"]
            longitude = row["LONGITUDE"]

            query = """
            MERGE (d:District {name:$district})

            MERGE (m:Mandal {name:$mandal})
            MERGE (d)-[:HAS_MANDAL]->(m)

            MERGE (l:Location {lgd_code:$lgd_code})

            SET
                l.name=$location_name,
                l.type=$location_type,
                l.latitude=$latitude,
                l.longitude=$longitude

            MERGE (m)-[:HAS_LOCATION]->(l)
            """

            session.run(
                query,
                district=district,
                mandal=mandal,
                lgd_code=lgd_code,
                location_name=location_name,
                location_type=location_type,
                latitude=latitude,
                longitude=longitude
            )

    print("Locations imported successfully")

    def import_nodes():
    pass


def import_services():
    pass


def import_ont_to_olt():
    pass


def import_olt_to_router():
    pass


def import_child_parent():
    pass

    def main():

    import_locations()

    import_nodes()

    import_services()

    import_ont_to_olt()

    import_olt_to_router()

    import_child_parent()


if __name__ == "__main__":
    main()