import { useEffect, useState } from "react";
import { ScrollView, View, Text, StyleSheet, Image } from "react-native";

const LittleBabyWidget = ({ title, children }) => {
  return (
    <View style={babyStyles.container}>
      <Text style={babyStyles.title}>{title}</Text>
      <View style={babyStyles.content}>{children}</View>
    </View>
  );
};

const babyStyles = StyleSheet.create({
  container: {
    padding: 10,
    backgroundColor: "#aabbff",
    borderRadius: 10,
    width: 180,
    height: 180,
    flexDirection: "column",
  },
  title: {
    fontSize: 24,
    fontWeight: "bold",
    marginBottom: 10,
  },
  content: {},
});

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
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>{data.nearest_area[0].areaName[0].value}</Text>
      <View style={styles.iconContainer}>
        {data.current_condition[0].weatherIconUrl[0].value && (
          <Image
            source={{
              uri: data.current_condition[0].weatherIconUrl[0].value,
            }}
            style={{ width: 100, height: 100 }}
          />
        )}
        <Text style={styles.currentTemp}>
          {data.current_condition[0].temp_F}°F
        </Text>
      </View>
      <Text style={styles.description}>
        {data.current_condition[0].weatherDesc[0].value}
      </Text>
      <View style={styles.extremesContainer}>
        <Text style={styles.extremeText}>
          High: {data.weather[0].maxtempF}°F
        </Text>
        <Text style={styles.extremeText}>
          Low: {data.weather[0].mintempF}°F
        </Text>
      </View>
      <View style={styles.babyContainer}>
        <LittleBabyWidget title="Wind">
          <Text style={styles.babyText}>
            Speed: {data.current_condition[0].windspeedMiles} mph
          </Text>
          <Text style={styles.babyText}>
            Direction: {data.current_condition[0].winddir16Point}
          </Text>
        </LittleBabyWidget>
        <LittleBabyWidget title="Atmosphere">
          <Text style={styles.babyText}>
            Humidity: {data.current_condition[0].humidity}%
          </Text>
          <Text style={styles.babyText}>
            Pressure: {data.current_condition[0].pressure} in
          </Text>
          <Text style={styles.babyText}>
            Visibility: {data.current_condition[0].visibilityMiles} mi
          </Text>
        </LittleBabyWidget>
      </View>
      <View style={styles.babyContainer}>
        <LittleBabyWidget title="Sun">
          <Text style={styles.babyText}>
            Rise: {data.weather[0].astronomy[0].sunrise}
          </Text>
          <Text style={styles.babyText}>
            Set: {data.weather[0].astronomy[0].sunset}
          </Text>
        </LittleBabyWidget>
        <LittleBabyWidget title="Moon">
          <Text style={styles.babyText}>
            Rise: {data.weather[0].astronomy[0].moonrise}
          </Text>
          <Text style={styles.babyText}>
            Set: {data.weather[0].astronomy[0].moonset}
          </Text>
        </LittleBabyWidget>
      </View>
      <View style={styles.babyContainer}>
        <LittleBabyWidget title="Precipitation">
          <Text style={styles.babyText}>
            Chance: {data.weather[0].hourly[0].chanceofrain}%
          </Text>
          <Text style={styles.babyText}>
            Amount: {data.weather[0].hourly[0].precipMM} mm
          </Text>
        </LittleBabyWidget>
        <LittleBabyWidget title="UV Index">
          <Text style={styles.babyText}>Index: {data.weather[0].uvIndex}</Text>
        </LittleBabyWidget>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flexDirection: "column",
    alignItems: "center",
    backgroundColor: "#ddddff",
  },
  title: {
    fontSize: 48,
    fontWeight: "bold",
    marginTop: 20,
  },
  iconContainer: {
    flexDirection: "row",
  },
  currentTemp: {
    fontSize: 48,
    marginTop: 20,
  },
  description: {
    fontSize: 24,
    marginBottom: 20,
  },
  extremesContainer: {
    flexDirection: "row",
    justifyContent: "space-around",
    width: "100%",
    paddingHorizontal: 20,
    marginBottom: 20,
  },
  extremeText: {
    fontSize: 24,
  },
  babyContainer: {
    width: "100%",
    height: 200,
    flexDirection: "row",
    justifyContent: "space-around",
  },
  babyText: {
    fontSize: 18,
  },
});

export default WeatherScreen;
