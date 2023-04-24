import FullWidthLayout from "@hocs/FullWidthLayout";
import { connect } from "react-redux";

const Home = () => {
  return (
    <>
      <h1>hola</h1>
      <FullWidthLayout>HOme</FullWidthLayout>
    </>
  );
};

const mapStatetoProps = (state) => ({});

export default connect(mapStatetoProps, {})(Home);
