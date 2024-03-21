import { useEffect, useState } from "react";
import { View, Text, StyleSheet } from "react-native";

const WeatherScreen = () => {
    const [data, setData] = useState(null);

    useEffect(() => {
        fetch("https://wttr.in/?format=j1").then((response) => {
            response.json().then((data) => {
                setData(data);
            });
        });
    }, []);

    if (!data) {
        return null;
    }

    return (
        <View style={styles.container}>
            <Text style={styles.text}>{data.nearest_area[0].areaName[0].value}</Text>
            <Text style={styles.text}>{data.current_condition[0].weatherDesc[0].value}</Text>
            <Text style={styles.text}>{data.current_condition[0].temp_C}°C</Text>
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
    },
    text: {
        fontSize: 24,
    },
});

export default WeatherScreen;
