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

      <div className="bg-wallpaper">
        {/* Landing Page */}
        <div className="md:container md:mx-auto w-full h-screen flex flex-col justify-center py-4">
          <nav className="flex justify-between items-center py-4">
            <div className="jobhub-logo">
              <img src="/images/Jobhub Logo.png" alt="Job Hub" className="w-60"/> 
            </div>
            <div className="flex space-x-16">
              <a href="#jobs" className="hover:bg-custom-black text-white px-6 py-2 rounded-full ">Jobs</a>
              <a href="#about" className="hover:bg-custom-black text-white px-6 py-2 rounded-full ">About Us</a>
              <a href="#login" className="hover:bg-custom-black text-white px-6 py-2 rounded-full border">Log In</a>
            </div>
          </nav>
          <div className="flex flex-1 mt-[10%]"> {/* Using margin to solve for now */}
            <div className="w-1/2">
              <div className="relative w-full">
                <Image 
                src="/images/Jobhub Landing.svg" // Path to your SVG
                alt="Dream Companies"
                layout="responsive"
                width={685}
                height={204}
                />
              </div>
            </div>
            <div className="w-1/2 text-center space-y-6 px-12">
              <h1 className="text-4xl font-bold">Your Career Starts Here! &#9654;</h1>
              <p className="text-xl text-center">
                Unleash your potential with real-world experiences. Explore, learn, and grow with our
                diverse internship opportunities.
              </p>
              <div className="flex justify-center items-center space-x-6 ">
                <button className="bg-custom-black hover:bg-custom-orange text-white font-semibold py-2 px-4 rounded-full">
                  Find Job
                </button>
                <button className="bg-custom-gray hover:bg-custom-orange text-white font-semibold hover:text-white py-2 px-4 rounded-full">
                  Learn More
                </button>
              </div>
            </div>
          </div>
          {/* Dare to Dream Section */}
          <div className="flex justify-center items-center w-full"> {/* Using image for now, will use the actual logo and texts*/}
            <div className="relative w-full">
              <Image 
              src="/images/Dream Logo.svg" // Path to your SVG
              alt="Dream Companies"
              layout="responsive"
              width={1442}
              height={281}
              />
            </div>
          </div>
        </div>


        {/* Jobs Section */}
        



      </div>
    </>
  );
};

export default HomePage;
