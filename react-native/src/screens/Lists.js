import React from "react";

import { Text, StyleSheet, View, Image, FlatList } from "react-native";

const SongListScreen = () => {
  const hello = "hello world";

  const songs = [
    { song: "On Top of The World", year: "2019" },
    { song: "Never Gonna Give You Up", year: "1987" },
    { song: "Eye of the Tiger", year: "1982" },
    { song: "Love Sosa", year: 2012 },
    { song: "Hallelujah", year: 2012 },
    { song: "Don't Like (Ft. Lil Reese)", year: 2012 },
    { song: "No Tomorrow", year: 2012 },
    { song: "Hate Bein' Sober (Ft. 50 Cent & Wiz Khalifa) ", year: 2012 },
    { song: "Kay Kay", year: 2012 },
    { song: "Laughin’ to the Bank", year: 2012 },
    { song: "Diamonds (Ft. French Montana)", year: 2012 },
    { song: "Ballin'", year: 2012 },
    { song: "Understand Me (Ft. Jeezy)", year: 2012 },
    { song: "Hunna (Album Version) (Ft. Rick Ross)", year: 2012 },
  ];

  return (
    <View>
      <Text style={styles.text}>SongList</Text>
      <FlatList
        data={songs}
        renderItem={({ item }) => {
          return (
            <Text style={styles.text}>
              {item.year} - {item.song}
            </Text>
          );
        }}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  text: {
    fontSize: 30,
  },
});

export default SongListScreen;
