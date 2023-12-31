import Head from 'next/head';
import Image from 'next/image';
import React from 'react';

const HomePage = () => {
  return (
    <>
      <Head>
        <title>Job Hub</title>
        <meta name="description" content="Find your dream job with Job Hub" />
      </Head>

      <div className="container mx-auto px-4 h-screen w-full flex flex-col justify-center">
        <nav className="flex justify-between items-center py-4">
          <div className="jobhub-logo">
            {/* Placeholder*/}
            <span>Logo</span>
          </div>
          <div className="flex space-x-4">
            <a href="#about" className="hover:underline">About Us</a>
            <a href="#jobs" className="hover:underline">Jobs</a>
            <a href="#login" className="hover:underline">Log In</a>
          </div>
        </nav>

        <div className="flex flex-1 items-center justify-center">
          {/* Placeholder*/}
          <div className="w-1/2">
            {/* Placeholder*/}
            <div className="wallpaper-image">
              <span>Placeholder</span>
            </div>
          </div>

          <div className="w-1/2 text-right space-y-6">
            <h1 className="text-6xl font-bold">Your Career Starts Here!</h1>
            <p className="text-xl">
              Unleash your potential with real-world experiences. Explore, learn, and grow with our
              diverse internship opportunities.
            </p>
            <div className="space-x-4">
              <button className="bg-yellow-500 hover:bg-yellow-700 text-white font-bold py-2 px-4 rounded">
                Find Job
              </button>
              <button className="bg-transparent hover:bg-yellow-500 text-yellow-700 font-semibold hover:text-white py-2 px-4 border border-yellow-500 hover:border-transparent rounded">
                Learn More
              </button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default HomePage;
