import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'dynamicTime'
})
export class DynamicTimePipe implements PipeTransform {

  transform(seconds: number, startDate: Date): number {
    console.log(seconds);
    console.log(startDate);
    
    const currentDate = new Date();
    const startTime = new Date(startDate).getTime() / 1000; // Başlangıç tarihini saniyeye çevir

    // Şu anki tarihi saniyeye çevir ve başlangıç tarihinden çıkart
    const remainingSeconds = Math.floor(startTime + seconds - currentDate.getTime() / 1000);

    // Geri sayım sırasındaki saniyeleri diziye dönüştür
    return remainingSeconds;
  }

}
