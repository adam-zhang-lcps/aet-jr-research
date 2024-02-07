import { createAppContainer } from "react-navigation";
import { createStackNavigator } from "react-navigation-stack";
import HomeScreen from "./src/screens/HomeScreen";
import CuteAnimals from "./src/screens/CuteAnimals";
import SongListScreen from "./src/screens/Lists";
import Counter from "./src/screens/Counter";
import StylingBoxScreen from "./src/screens/StylingBoxScreen";
import NorwayFlag from "./src/screens/NorwayFlag";

const navigator = createStackNavigator(
  {
    Home: HomeScreen,
    CuteScreen: CuteAnimals,
    SongListScreen: SongListScreen,
    Counter: Counter,
    StylingBoxScreen: StylingBoxScreen,
    NorwayFlag: NorwayFlag,
  },
  {
    initialRouteName: "Home",
    defaultNavigationOptions: {
      title: "App",
    },
  },
);

export default createAppContainer(navigator);
