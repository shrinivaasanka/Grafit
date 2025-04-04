use std::env;
use std::io::*;
use std::time::*;
use rayon::prelude::*;
use foreach::*;
use std::collections::HashSet;
use std::iter::FromIterator;

static mut factors: Vec<i64> = Vec::new();

fn main() {
    let args: Vec<String>=env::args().collect();
    let number_to_factorize: i64=args[1].parse().unwrap(); 
    let range: i64=args[2].parse().unwrap();
    let rasterization: String=args[3].clone();
    factorize_multipleintegers(number_to_factorize,range,rasterization);
    unsafe {
        //println!("main():Factors of {number_to_factorize} are {:#?} ",factors);
        let factorsset: HashSet<i64> = HashSet::from_iter(factors.clone());
        println!("main():Set of Factors of {number_to_factorize} are {:#?} ",factorsset);
    }
    stdout().flush().unwrap();
    //pariter64bits();
}

fn pariter64bits() {
    let mut len : i64 = 10000;
    let mut vector = 1 .. len;
    vector.par_bridge().for_each(|paritem| {
        println!("item {:#?} :",paritem);
    });
}

fn factorize_multipleintegers(num_fact:i64,range:i64,rasterization:String) {
    let mut i = 0;
    let mut runtimes = Vec::new();
    for i in 0..range {
        let mut systemtimebegin = SystemTime::now();
        let mut number_to_factorize = num_fact+i;
        let mut raster = rasterization.clone();
        println!("Factorization of {number_to_factorize} began in (nanoseconds): {:#?} ",systemtimebegin);
        rasterize_hyperbolic_arc(number_to_factorize,raster);
        let systemtimeend = SystemTime::now();
        let duration = systemtimeend.duration_since(systemtimebegin).unwrap(); 
        println!("Factorization of {number_to_factorize} was completed in (nanoseconds): {:#?} ",duration);
        runtimes.push(duration);
    }
}

#[inline]
fn rasterize_hyperbolic_arc(num_fact: i64,rasterization: String) -> i64
{
    let mut y1 = 1..num_fact-1;
    let mut y2 = 1..num_fact-1;
    if rasterization=="sequential"
    {
        let systemtimebegin = SystemTime::now();
        y1.foreach(|item,iter| {
            let mut xtile_start = num_fact/item;
            let mut xtile_end = num_fact/(item+1);
            println!("tile segment {item}: from {xtile_start} to {xtile_end}");
            binary_search(num_fact,xtile_end,item,xtile_start,item);
        });
        let systemtimeend = SystemTime::now();
        let duration = systemtimeend.duration_since(systemtimebegin).unwrap(); 
        println!("Sequential Rasterization phase of factoring {num_fact} was completed in (nanoseconds): {:#?} ",duration);
        stdout().flush().unwrap();
    }
    if rasterization=="parallel"
    {
        let systemtimebegin = SystemTime::now();
        let numberofbits = num_fact.ilog2();
        println!("Size of integer to be factorized (in bits): {numberofbits}");
        if numberofbits <= 32 
        {
            y2.into_par_iter().for_each(|paritem| {
                let mut xtile_start = num_fact/paritem;
                let mut xtile_end = num_fact/(paritem+1);
                //println!("tile segment {paritem}: from {xtile_start} to {xtile_end}");
                binary_search(num_fact,xtile_end,paritem,xtile_start,paritem);
            });
        }
        else
        {
            y2.par_bridge().for_each(|paritem| {
                let mut xtile_start = num_fact/paritem;
                let mut xtile_end = num_fact/(paritem+1);
                //println!("tile segment {paritem}: from {xtile_start} to {xtile_end}");
                binary_search(num_fact,xtile_end,paritem,xtile_start,paritem);
            });
        }
        let systemtimeend = SystemTime::now();
        let duration = systemtimeend.duration_since(systemtimebegin).unwrap(); 
        println!("Parallel Rasterization phase of factoring {num_fact} was completed in (nanoseconds): {:#?} ",duration);
        stdout().flush().unwrap();
    }
    return 1;
}

#[inline]
//fn binary_search(num_fact:i64,xl:i64,yl:i64,xr:i64,yr:i64) -> Vec<i64> 
fn binary_search(num_fact:i64,xl:i64,yl:i64,xr:i64,yr:i64)
{
    //println!("binary seach of rasterized hyperbolic arc bow tilesegment xy = {num_fact}: {xl},{yl},{xr},{yr}");
    let mut xl_clone = xl.clone();
    let mut yl_clone = yl.clone();
    let mut xr_clone = xr.clone();
    let mut yr_clone = yr.clone();
    //let mut factors = Vec::new();
    while xl_clone <= xr_clone
    {
        let mut midpoint = (xl_clone + xr_clone) / 2;
        //println!("Midpoint = {midpoint}");
        let mut factorcandidate = midpoint*yl_clone;
        //println!("Factor candidate point : {factorcandidate}");
        //println!("===============================================================");
        if xl_clone==xr_clone
        {
             //std::process::exit(1);
             unsafe {
                //println!("1.Factors of {num_fact} are {:#?} ",factors);
                //return factors;
             }
        }
        if factorcandidate==num_fact
        {
             let systemtimenow = SystemTime::now();
             println!("Factor point located : {midpoint} , {yl_clone} at {:#?} nanoseconds",systemtimenow);
             unsafe {
                factors.push(factorcandidate);
                //println!("2.Factors of {num_fact} are {:#?} ",factors);
             }
        }
        if xl_clone*yl_clone==num_fact
        {
             let systemtimenow = SystemTime::now();
             println!("Factor point located : {xl_clone} , {yl_clone} at {:#?} nanoseconds",systemtimenow);
             unsafe {
                factors.push(xl_clone);
                factors.push(yl_clone);
                //println!("3.Factors of {num_fact} are {:#?} ",factors);
             }
        }
        if xr_clone*yr_clone==num_fact
        {

             let systemtimenow = SystemTime::now();
             println!("Factor point located : {xr_clone} , {yr_clone} at {:#?} nanoseconds",systemtimenow);
             unsafe {
                factors.push(xr_clone);
                factors.push(yr_clone);
                //println!("4.Factors of {num_fact} are {:#?} ",factors);
             }
        }
        if factorcandidate > num_fact
        {
             //println!("factorcandiate > num_fact");
             xr_clone = xl_clone + midpoint;
        }
        else
        {
             //println!("factorcandiate < num_fact");
             xl_clone = xl_clone + midpoint;
        }
        //println!("===============================================================");
    }
    stdout().flush().unwrap();
    unsafe {
        //println!("5.Factors of {num_fact} are {:#?} ",factors);
        //return factors;
    }
}
