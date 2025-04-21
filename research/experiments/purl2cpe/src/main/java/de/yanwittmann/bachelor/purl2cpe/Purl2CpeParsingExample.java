package de.yanwittmann.bachelor.purl2cpe;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class Purl2CpeParsingExample {

    private static final String URL = "jdbc:sqlite:data/purl2cpe.db";

    public static void main(String[] args) throws Exception {
        int uniquePurlsCount = countUniquePurls();
        System.out.println("Unique purl count: " + uniquePurlsCount);
    }

    public static int countUniquePurls() throws Exception {
        String query = "SELECT COUNT(DISTINCT purl) FROM purl2cpe";
        try (Connection conn = getConnection();
             PreparedStatement stmt = conn.prepareStatement(query);
             ResultSet rs = stmt.executeQuery()) {

            if (rs.next()) {
                return rs.getInt(1);
            }
        }
        return 0;
    }

    private static Connection getConnection() throws Exception {
        return DriverManager.getConnection(URL);
    }
}
