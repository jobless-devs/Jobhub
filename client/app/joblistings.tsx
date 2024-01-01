'use client'

import Link from 'next/link';
import React, { useEffect, useState } from 'react';

// Define Type for Job Card
type Job = {
  id: number;
  date: string;
  position: string;
  company: string;
  location: string;
  link: string;
};

type JobListingsProps = {
  onBack: () => void; // Function to handle going back to the landing page
};

const JobListings = ({onBack}: JobListingsProps) => {
  const [jobs, setJobs] = useState<Job[]>([]);

  // Placeholder data for the job cards
  // Replace this with your data fetching logic
  useEffect(() => {
    const fetchJobs = async () => {
      // Replace with actual data fetching from your database
      const fetchedJobs = [
        {
          id: 1,
          date: "2023-03-01",
          position: "Software Engineer",
          company: "Company A",
          location: "New York, NY",
          link: "#"
        },
        // More Job Cards
      ];
      setJobs(fetchedJobs);
    };

    fetchJobs();
  }, []);

  return (
    <div className="container mx-auto p-4">
      <button onClick={onBack} className="bg-gray-200 hover:bg-gray-300 text-black font-bold py-2 px-4 rounded m-2">
        Back to Landing Page
      </button> 
      <h1 className="text-center text-3xl font-bold my-6">Job Listings</h1>
      <div className="flex justify-between items-center mb-6">
        <input
          type="text"
          placeholder="Search jobs..."
          className="border-2 border-gray-300 p-2 rounded-lg w-full md:w-1/2"
        />
        <div className="flex space-x-2 ml-4">
          {/* Filter buttons or dropdowns */}
          <div className="p-2 border-2 border-gray-300 rounded-lg">Filter 1</div>
          <div className="p-2 border-2 border-gray-300 rounded-lg">Filter 2</div>
          <div className="p-2 border-2 border-gray-300 rounded-lg">Filter 3</div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {jobs.map(job => (
          <Link href={job.link} key={job.id}>
              <h2 className="font-bold text-xl">{job.position}</h2>
              <p>{job.company}</p>
              <p>{job.location}</p>
              <p>{job.date}</p>
          </Link>
        ))}
      </div>
    </div>
  );
};

export default JobListings;
