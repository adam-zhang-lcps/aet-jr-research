import { createAppContainer } from "react-navigation";
import { createStackNavigator } from "react-navigation-stack";
import HomeScreen from "./src/screens/HomeScreen";
import CuteAnimals from "./src/screens/CuteAnimals";
import SongListScreen from "./src/screens/Lists";
import Counter from "./src/screens/Counter";
import StylingBoxScreen from "./src/screens/StylingBoxScreen";
import NorwayFlag from "./src/screens/NorwayFlag";
import ThePredictor from "./src/screens/ThePredictor";
import ImageScreen from "./src/screens/ImageScreen";
import Counters from "./src/screens/Counters";
import SimpleCalculator from "./src/components/SimpleCalculator";
import FullCalculator from "./src/screens/FullCalculator";
import FoodieScreen from "./src/screens/FoodieScreen";
import YelpBusinessDetails from "./src/screens/YelpBusinessDetails";
import WeatherScreen from "./src/screens/WeatherScreen";

const navigator = createStackNavigator(
  {
    Home: HomeScreen,
    CuteScreen: CuteAnimals,
    SongListScreen,
    Counter,
    StylingBoxScreen,
    NorwayFlag,
    ThePredictor,
    ImageScreen,
    Counters,
    SimpleCalculator,
    FullCalculator,
    FoodieScreen,
    YelpBusinessDetails,
    WeatherScreen,
  },
  {
    initialRouteName: "Home",
    defaultNavigationOptions: {
      title: "App",
    },
  },
);

export default createAppContainer(navigator);
