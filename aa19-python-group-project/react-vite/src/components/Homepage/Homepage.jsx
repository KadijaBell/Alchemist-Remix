
import "./Homepage.css";
import { useSelector } from "react-redux";

function Card({ title, description, className }) {
  return (
    <div className={`homepage-card ${className}`}>
      <h2>{title}</h2>
      <p>{description}</p>
    </div>
  );
}

function Homepage() {
  const user = useSelector((state) => state.session.user);
  return (
    <div className="homepage-container">
      <header className="homepage-header">
        <h1>✨Hi {user?.username || "Guest"}! Welcome to Alchemy Fusion✨</h1>
        <p>Transforming creativity into reality.</p>
      </header>

      <main className="homepage-main">
        <section className="homepage-section">
          <Card
            title="Explore Sources"
            description="Discover creative content curated for you."
            className="yellow-card"
          />
          <Card
            title="Create Fusions"
            description="Combine ideas and transform them into something new."
            className="orange-card"
          />
          <Card
            title="Share Reflections"
            description="Engage with the community and share your thoughts."
            className="green-card"
          />
        </section>
      </main>

      <footer className="homepage-footer">
        <p>✨Happy Alchemizing! ✨</p>
      </footer>
    </div>
  );
}

export default Homepage;


//import "./Homepage.css";
// import { useEffect} from "react";
// import { useSelector, useDispatch } from "react-redux";
// import {fetchFusions} from "../../redux/fusions";

// const Homepage = () => {
//   const dispatch = useDispatch();
//   const { list: fusions = [], status, error } = useSelector((state) => state.fusions || {});

//   useEffect(() => {
//     if (status === 'idle') {
//       dispatch(fetchFusions());
//     }
//   }, [dispatch, status]);

//   if (status === 'loading') return <p>🧪Loading fusions...🧪</p>;
//   if (status === 'failed') return <p>Error: {error}</p>;

//   return (
//     <div className="homepage">
//       <header className="homepage-header">
//         <h1>Discover Featured Fusions</h1>
//       </header>
//       <section className="fusion-section">
//         <h2>Featured Fusions</h2>
//         <div className="fusion-cards">
//           {fusions.map((fusion) => (
//             <div key={fusion.id} className="fusion-card">
//               <h3>{fusion.name}</h3>
//               <p>{fusion.description || "No description available"}</p>
//             </div>
//           ))}
//         </div>
//       </section>
//     </div>
//   );
// };

// export default Homepage;

// function Homepage() {
//   return (
//     <div className="homepage-container">
//       <header className="homepage-header">
//         <h1>Welcome to Alchemy Fusion</h1>
//         <p>Transforming creativity into reality.</p>
//       </header>
//       <main className="homepage-main">
//         <div className="homepage-card yellow-card">
//           <h2>Explore Sources</h2>
//           <p>Discover creative content curated for you.</p>
//         </div>
//         <div className="homepage-card orange-card">
//           <h2>Create Fusions</h2>
//           <p>Combine ideas and transform them into something new.</p>
//         </div>
//         <div className="homepage-card green-card">
//           <h2>Share Reflections</h2>
//           <p>Engage with the community and share your thoughts.</p>
//         </div>
//       </main>
//       <footer className="homepage-footer">
//         <p>Start your journey today ✨</p>
//       </footer>
//     </div>
//   );
// }
// export default Homepage;
