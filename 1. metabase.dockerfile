FROM metabase/metabase:latest

# Copy the Dremio JDBC driver JAR file into the Metabase image
COPY dremio.metabase-driver.jar /plugins/dremio.metabase-driver.jar