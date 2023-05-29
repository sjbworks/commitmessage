// import express from "express";
// import http from "http";

import openai from "openai";
openai.api_key = process.env.OPENAI_API_KEY;

async function maliculousChecker() {
  console.log(process.env.OPENAI_API_KEY);
  const check = await openai.completions.create({
    model: "text-davinci-003",
    prompt: `Please answer yes or no if the following sentence is malicious: ${process.argv}`,
    temperature: 0.6,
  });
  console.log(check);
}

maliculousChecker();
